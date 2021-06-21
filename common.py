x_col_id = 0
y_col_id = 1
t_col_id = 2
q_col_id = 3


def sqr(x):
    return x*x

def angle_in_range(angle):
    if angle > 180:
        angle -= 360
    elif angle < -180:
        angle += 360

    return int(angle)


class Person:
    def __init__(self, name, surname, pId=-1):
        self.personId: int = pId
        self.name: str = name
        self.surname: str = surname


class Fingerprint:
    def __init__(self, ownerId=-1, mntsList=[]):
        self.ownerId: int = ownerId
        self.mntsList: list = mntsList
