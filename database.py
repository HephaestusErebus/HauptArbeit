import psycopg2
from psycopg2 import Error
from common import Person, Fingerprint
from common import x_col_id, y_col_id, t_col_id

def mntsListToStringView(mntsList:list):
    strList = ['{0} {1} {2}'.format(mnt[x_col_id], mnt[y_col_id], mnt[t_col_id]) for mnt in mntsList]
    return '\n'.join([str for str in strList])

def strViewToMntsList(strView:str):
    strList = strView.split('\n')
    return [line.split(' ') for line in strList]

def prsnTuplesToList(prsnTuples: list):
    return [Person(tuple[1], tuple[2], tuple[0]) for tuple in prsnTuples]

def fngrTuplesToList(fngrTuples: list):
    return [Fingerprint(tuple[0], strViewToMntsList(tuple[1])) for tuple in fngrTuples]


class DatabaseController:
    connection = None
    cursor = None
    def __init__(self):
        self.connect(db_name='Fingerprints DB')

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def connect(self, db_name, hostname='localhost', port='5432', user='postgres', password='root'):
        try:
            self.connection = psycopg2.connect(user=user, password=password, host=hostname,
                                               port=port, database=db_name)
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print('Postgresql connection error', error)

    def addPerson(self, person: Person):
        try:
            query = 'SELECT COALESCE((SELECT MAX(id) +1 FROM persons), 1);'
            self.cursor.execute(query)
            id = self.cursor.fetchone()

            query = 'INSERT INTO persons (id, name, surname) VALUES (%s, %s, %s);'
            item_tuple = (id, person.name, person.surname)
            self.cursor.execute(query, item_tuple)
            self.connection.commit()

        except (Exception, Error) as error:
            print('Postgresql add person error', error)

    def getPersons(self):
        try:
            query = 'SELECT id, name, surname FROM persons ORDER BY surname DESC, name;'
            self.cursor.execute(query)
            prsnTuples = self.cursor.fetchall()
            return prsnTuplesToList(prsnTuples)

        except (Exception, Error) as error:
            print('Postgresql select persons error', error)

    def getPersonName(self, personId):
        try:
            query = 'SELECT name, surname FROM persons WHERE id = %s;'
            self.cursor.execute(query, personId)
            prsnTuple = self.cursor.fetchone()
            return '{0} {1}'.format(prsnTuple[1], prsnTuple[0])

        except (Exception, Error) as error:
            print('Postgresql select persons error', error)

    def addFingerprint(self, fingerData: Fingerprint):
        try:
            query = 'SELECT COALESCE((SELECT MAX(id) +1 FROM fingerprints), 1);'
            self.cursor.execute(query)
            id = self.cursor.fetchone()

            query = 'INSERT INTO fingerprints (id, person_id, minutae_points_count, minutae_points_set) ' \
                    'VALUES (%s, %s, %s, %s);'

            data_tuple = (id, fingerData.ownerId, len(fingerData.mntsList), mntsListToStringView(fingerData.mntsList))
            self.cursor.execute(query, data_tuple)
            self.connection.commit()

        except (Exception, Error) as error:
            print('Postgresql add fingerprint error', error)


    def getFingerprints(self, startPos, maxCount):
        try:
            query = "SELECT person_id, minutae_points_set " \
                    "FROM fingerprints " \
                    "ORDER BY person_id DESC, id DESC " \
                    "LIMIT %s OFFSET %s;"

            data_tuple = (maxCount, startPos)
            self.cursor.execute(query, data_tuple)
            fngrTuples = self.cursor.fetchall()
            return fngrTuplesToList(fngrTuples)

        except (Exception, Error) as error:
            print('Postgresql select fingerprints from {0} to {1} error'.format(startPos, startPos+maxCount), error)
