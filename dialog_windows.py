from PyQt5.QtWidgets import QWidget, QDialog

from person_selection import Ui_person_selection
from add_user import Ui_add_user
from result import Ui_result

from database import DatabaseController
from common import Person, Fingerprint

class addUserDialog(QDialog, Ui_add_user):
    def __init__(self, dbController: DatabaseController):
        super(addUserDialog, self).__init__()
        self.setupUi(self)
        self.dbController = dbController
        self.connectSlots()

    def connectSlots(self):
        self.addPerson_pB.clicked.connect(self.addPersonToDatabase)
        self.cancel_pB.clicked.connect(self.close)

    def addPersonToDatabase(self):
        newPerson = Person(self.personName_lE.text(), self.personSurname_lE.text())
        self.dbController.addPerson(newPerson)
        self.close()

    def getPersonData(self):
        self.personName_lE.clear()
        self.personSurname_lE.clear()
        self.show()


class selectPersonDialog(QDialog, Ui_person_selection):

    def __init__(self, dbController: DatabaseController):
        super(selectPersonDialog, self).__init__()
        self.setupUi(self)
        self.connectSlots()
        self.dbController = dbController

    def connectSlots(self):
        self.selectPerson_pB.clicked.connect(self.saveToDatabase)
        self.cancel_pB.clicked.connect(self.close)

    def saveToDatabase(self):
        curPersonId = self.persons_lst.currentRow()
        if curPersonId >= 0 and len(self.persons_lst) >= curPersonId:
            curFingerprintData = Fingerprint()
            curFingerprintData.ownerId = self.prsnList[curPersonId].personId
            curFingerprintData.mntsList = self.mntsList
            self.dbController.addFingerprint(curFingerprintData)
            self.close()


    def selectOwner(self, mntsList):
        self.mntsList = mntsList
        self.prsnList = self.dbController.getPersons()
        self.addPersonsOnForm()
        self.show()

    def addPersonsOnForm(self):
        self.persons_lst.clear()
        for person in self.prsnList:
            self.persons_lst.addItem('{0} {1}'.format(person.surname, person.name))


class showResultDialog(QDialog, Ui_result):
    def __init__(self):
        super(showResultDialog, self).__init__()
        self.setupUi(self)
        self.connectSlots()

    def connectSlots(self):
        self.ok_pB.clicked.connect(self.close)

    def showMatchResult(self, result: str):
        self.result_lbl.setText(result)
        self.show()
