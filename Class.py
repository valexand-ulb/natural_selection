from Settings import *
from os import name as os_name
from os import system as os_system
from random import choice as random_choice
from time import sleep


class Game:
    def __init__(self):
        self.play = Plateau()
        self.play.showMat()
        sleep(1.5)
        #while self.play.food_list:
        for i in range(5):
            for mob in self.play.mob_list:
                if mob.getCoord() is not None:
                    mob.ThinkedMove(self.play.plateau)
                self.play.updateFoodList()
                self.play.showMat()
                sleep(1.5)


class Plateau:
    def __init__(self):
        self.plateau = [[0 for j in range(MAT_SIZE)] for i in range(MAT_SIZE)]
        self.mat_size = len(self.plateau)

        self.food_list = [Food(FPOSITIONS[j], 4, j) for j in range(len(FPOSITIONS))]
        self.mob_list = [Mob(MPOSITION[i], 12, i) for i in range(len(MPOSITION))]
        self.updateFoodList()

        for mob in self.mob_list:
            x, y = mob.getCoord()
            self.plateau[x][y] = mob
        for elem in OPOSITION:
            x, y = elem
            self.plateau[x][y] = 1

    def updateFoodList(self):
        to_rem = []
        for food in self.food_list:
            if food.getCoord() is not None:
                x, y = food.getCoord()
                self.plateau[x][y] = food
            else:
                to_rem.append(food)

        for elem in to_rem:
            self.food_list.remove(elem)

    def showMat(self, c=True):
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
                    s += ' . '
            s += '\n\n'

        if c:
            if os_name == 'nt':
                os_system('cls')
            elif os_name == 'posix':
                os_system('clear')
        print(s)


class Mob:
    def __init__(self, position, energy, id, speed=1, consumption=1, scope=2):
        self.id = id

        self.coord = position
        self.energy = energy
        self.speed = speed
        self.energy_consumption = consumption
        self.scope = scope

    def getCoord(self):
        return self.coord

    def getMobEnergy(self):
        return self.energy

    def earnEnergy(self, earn):
        self.energy += earn

    def loseEnergy(self, energy_consumption):
        self.energy -= energy_consumption

    def getID(self):
        return self.id

    def possible(self, plateau):
        mat_size = len(plateau)
        x, y = self.coord if self.coord is not None else (-1, -1)

        possible = []

        vect_list = [(i, j) for i in range(-1, 2, 1) for j in range(-1, 2, 1)]

        for vect in vect_list:
            i, j = vect
            if 0 <= x+i < mat_size and 0 <= y+j < mat_size:
                if plateau[x+i][y+j] == 0 or type(plateau[x+i][y+j]) == Food:
                    possible.append((x+i, y+j))
        return possible

    def Think(self, plateau, profondeur):

        possible = self.possible(plateau)
        old_coord = self.coord

        score = 0
        f = []
        for elem in possible:
            x, y = elem
            if type(plateau[x][y]) == Food:
                f.append((x, y))
        score = len(f)

        if profondeur == 0:
            return None, score

        best_score = -1000
        best_move = []

        finni = False
        i = 0
        while not finni and i < len(possible):
            coord = possible[i]
            if type(plateau[coord[0]][coord[1]]) != Food:
                self.Move(coord, plateau, True)
                score = self.Think(plateau, profondeur-1)[1]

                if best_score < score:
                    best_score = score
                    best_move = [(coord, score)]
                elif score == best_score:
                    best_move.append((coord, score))

                self.Move(old_coord, plateau, True)
            else:
                best_score = score
                best_move = [(coord, score)]
                finni = True
            i+= 1
        return random_choice(best_move)

    def Move(self, new_coord, plateau, emulated=False):
        if new_coord != self.coord:
            plateau[self.coord[0]][self.coord[1]] = 0
            self.coord = new_coord

            if type(plateau[self.coord[0]][self.coord[1]]) == Food and not emulated:
                plateau[self.coord[0]][self.coord[1]].removeCoord()
                self.earnEnergy(plateau[self.coord[0]][self.coord[1]].getEnergy())

            plateau[self.coord[0]][self.coord[1]] = self
            self.loseEnergy(self.energy_consumption)

    def ThinkedMove(self, plateau):
        choice = self.Think(plateau, self.scope)[0]
        print('Mob {} moved from {} to {}'.format(self.id+1, self.coord, choice))
        self.Move(choice, plateau)


class Food:
    def __init__(self, position, energy, id, is_poison=False):
        self.id = id

        self.coord = position
        self.given_energy = energy

    def getCoord(self):
        return self.coord

    def removeCoord(self):
        self.coord = None

    def getEnergy(self):
        return self.given_energy


if __name__ == '__main__':
    Game()
