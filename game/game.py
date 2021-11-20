from random import randint

class Hero:
    def __init__(self):
       self.__power = 25
       print("Герой вступил в игру.")

    def buf(self, artefact):
        self.__power = self.__power + artefact
        print("Герой получил усиление на", artefact, "очков.")

    def power(self):
        return self.__power

class Monster:
    def __init__(self, value):
        self.__power = value

    def power(self):
        return self.__power

class Artefact:
    def __init__(self, value):
        self.__power = value

    def power(self):
        return self.__power


hero = Hero()
levelList = [randint(0, 1) for i in range(10)] # 0 - monster, 1 - artefact

count = 1
for level in levelList:
    if level == 0:
        monster = Monster(randint(5, 100))
        print("В зале находится монстр силой", monster.power())
        if hero.power() >= monster.power():
            print("Герой победил монстра силой", monster.power())
            count += 1
        else:
            print("Герой проиграл на", count, "уровне.")
            exit()
    else:
        artefact = Artefact(randint(10, 80))
        print("В зале лежит артефакт силой", artefact.power())
        hero.buf(artefact.power())

print("Герой прошёл все залы с силой", hero.power())
