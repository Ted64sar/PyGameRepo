class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    def __init__(self):
        self.flag = True

    def sound(self):
        if self.flag:
            print('ding')
            self.flag = False
        else:
            self.flag = True
            print('dong')


class BellTower:
    def __init__(self, *kolokola):
        self.kolokola = list(kolokola)

    def append(self, new):
        self.kolokola.append(new)

    def sound(self):
        for zvon in self.kolokola:
            zvon.sound()
        print('...')

class SizedBellTower:
    def __init__(self, *kolokola):
        self.kolokola = list(kolokola)

    def append(self, new):
        self.kolokola.append(new)

    def sound(self):
        for zvon in self.kolokola:
            zvon.sound()
        print('...')
