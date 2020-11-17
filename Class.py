from Settings import *
from os import name as os_name
from os import system as os_system
from time import sleep

class Game:
    def __init__(self):
        self.play = Plateau()
        for mob in self.play.mob_list:
            for i in range(3):
                mob.move(self.play.plateau)
                self.play.showMat()
                sleep(2)


class Plateau:
    def __init__(self):
        self.plateau = [[0 for j in range(MAT_SIZE)] for i in range(MAT_SIZE)]
        self.mat_size = len(self.plateau)

        self.food_list = [Food(FPOSITIONS[j], 4, j) for j in range(len(FPOSITIONS))]
        self.mob_list = [Mob(MPOSITION[i], 12, i) for i in range(len(MPOSITION))]

        for food in self.food_list:
            x, y = food.getCoord()
            self.plateau[x][y] = food
        for mob in self.mob_list:
            x, y = mob.getCoord()
            self.plateau[x][y] = mob
        for elem in OPOSITION:
            x, y = elem
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
                    s += ' . '
            s += '\n\n'

        if os_name == 'nt':
            os_system('cls')
        elif os_name == 'posix':
            os_system('clear')
        print(s)


class Mob:
    def __init__(self, position, energy, id, speed=1, consumption=1, scope=1):
        self.id = id

        self.coord = position
        self.energy = energy
        self.speed = speed
        self.energy_consumption = consumption
        self.scope = scope

    def getCoord(self):
        return self.coord


    def remCoord(self):
        self.coord = None

    def getEnergy(self):
        return self.energy

    def loseEnergy(self, energy_consumption):
        self.energy -= energy_consumption

    def getID(self):
        return self.id

    def think(self, plateau):
        mat_size = len(plateau)
        vect_card = [(i, j) for i in range(-1, 2, 1) for j in range(-1, 2, 1)]
        vect_card.remove((0, 0))

        x, y = self.coord
        selected_move = None
        possible = []
        for vect in vect_card:
            end = False
            i, j = vect
            while not end:
                new_x = x + i
                new_y = y + j

                # bool condition
                x_cond = 0 <= new_x < mat_size
                y_cond = 0 <= new_y < mat_size
                i_scope_cond = -self.scope <= i <= self.scope
                j_scope_cond = -self.scope <= j <= self.scope

                if x_cond and i_scope_cond and y_cond and j_scope_cond:
                    if type(plateau[new_x][new_y]) == Food:
                        selected_move = (new_x, new_y)

                    if i < 0:
                        i -= 1
                    elif i > 0:
                        i += 1

                    if j < 0:
                        j -= 1
                    elif j > 0:
                        j += 1
                    if plateau[new_x][new_y] == 0:
                        possible.append((new_x, new_y))
                else:
                    end = True
        if selected_move is None:
            res = possible[randint(0, len(possible)-1)]
        else:
            res = selected_move
        return res

    def move(self, plateau):
        choice = self.think(plateau)
        plateau[self.coord[0]][self.coord[1]] = 0
        self.coord = choice
        plateau[self.coord[0]][self.coord[1]] = self
        self.loseEnergy(self.energy_consumption)


class Food:
    def __init__(self, position, energy, id, is_poison=False):
        self.id = id

        self.coord = position
        self.given_energy = energy

    def getCoord(self):
        return self.coord

    def removeCoord(self):
        self.coord = None

if __name__ == '__main__':
    Game()