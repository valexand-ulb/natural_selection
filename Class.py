from Settings import *


class Mob:
    def __init__(self, position, pv, energy, id, speed=1, consumption=1, scope=1):
        self.id = id

        self.coord = position
        self.health = pv
        self.energy = energy
        self.speed = speed
        self.energy_consumption = consumption
        self.scope = scope

    def getCoord(self):
        return self.coord

    def setCoord(self, new_coord):
        self.coord = new_coord

    def remCoord(self):
        self.coord = None

    def getHealt(self):
        return self.health

    def loseHealth(self):
        self.health -= 1

    def getEnergy(self):
        return self.energy

    def loseEnergy(self):
        self.energy -= 1

    def getID(self):
        return self.id


class Food:
    def __init__(self, position, energy, id, is_poison=False):
        self.id = id

        self.coord = position
        self.given_energy = energy

    def getCoord(self):
        return self.coord

    def removeCoord(self):
        self.coord = None


class Plateau:
    def __init__(self):
        self.plateau = [[0 for j in range(MAT_SIZE)] for i in range(MAT_SIZE)]
        self.food_pos = []
        self.mob_pos = []
        self.placeItems()

    def placeItems(self):

        for k in range(len(FPOSITIONS)):
            x, y = FPOSITIONS[k]
            item = Food((x, y), randint(1, 4), k)
            self.plateau[x][y] = item
            self.food_pos.append(item)

        for l in range(len(MPOSITION)):
            x, y = MPOSITION[l]
            item = Mob((x, y), randint(10, 12), randint(10, 12), l)
            self.plateau[x][y] = item
            self.mob_pos.append(item)

        for k in range(len(OPOSITION)):
            x, y = MPOSITION[k]
            self.plateau[x][y] = 1

    def showMat(self):
        s = ""
        for line in self.plateau:
            for elem in line:
                if type(elem) == Mob:
                    s += MSIGN
                elif type(elem) == Food:
                    s += FSIGN
                elif elem == 1:
                    s += OSIGN
                else:
                    s += '  '
            s += '\n\n'
        print(s)


if __name__ == '__main__':
    p = Plateau()
    p.showMat()