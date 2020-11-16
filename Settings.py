from random import randint


class Position:
    def __init__(self):
        self.list = []
        read = self.readfile()

        letters = ''
        letters += [chr(i) for i in range(MAT_SIZE)]
        digit_list = [i for i in range(MAT_SIZE)]

        for i in range(len(read)):
            sublist = []
            for elem in read[i]:
                letter = elem[0]
                digit = int(elem[1])

                if digit in digit_list and letter in letters:
                    coord = (letters.index(letter), digit_list.index(digit))
                    sublist.append(coord)
            self.list.append(sublist)

    @staticmethod
    def readfile():
        with open('SetGame.txt') as openened_file:
            i = 0  # flag

            for line in openened_file:

                if i == 0:  # mob position
                    liste_mob = line.strip().split(',')
                    i += 1
                elif i == 1:  # obstacle
                    liste_obstacle = line.strip().split(',')
                    i += 1
        return liste_mob, liste_obstacle


class PositionFood(Position):
    def __init__(self):
        super().__init__()
        self.list = []
        for i in range(10):
            finni = False
            while not finni:
                x = randint(0, MAT_SIZE-1)
                y = randint(0, MAT_SIZE-1)
                if (x, y) not in self.list:
                    self.list.append((x, y))
                    finni = True

    def getList(self):
        return self.list


class PositionMob(Position):
    def __init__(self):
        super().__init__()
        self.newlist = self.list[0]

    def getList(self):
        return self.newlist


class PositionObstacle(Position):
    def __init__(self):
        super().__init__()
        self.newlist = self.list[2]

    def getList(self):
        return self.newlist


# Matrice
MAT_SIZE = 10

# Food
ENERGY = 4
FPOSITIONS = PositionFood().getList()

# Mob
MPOSITION = PositionMob().getList()

# Obstacle
MOBSTACLE = PositionObstacle.getList()

