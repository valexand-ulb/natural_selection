from random import randint


class Position:
    def __init__(self, choice):
        self.list = []
        read = self.readfile(choice)
        letters = [chr(97 + i) for i in range(MAT_SIZE)]

        for elem in read:
            letter = elem[0]
            digit = int(elem[1:])
            if letter in letters and 1<= digit <= MAT_SIZE:
                x = letters.index(letter)
                y = digit-1
                self.list.append((x, y))

    @staticmethod
    def readfile(choice):
        with open('SetGame.txt') as openened_file:
            liste_mob = []
            liste_obstacle = []
            liste_food = []
            finni = False
            i = 0
            for line in openened_file:
                if choice == 0 and i == 0 and not finni:  # mob position
                    liste_mob = line.strip().split(',')
                    finni = True
                elif choice == 1 and i == 1 and not finni:  # obstacle
                    liste_obstacle = line.strip().split(',')
                    finni = True
                elif choice == 2 and i == 2 and not finni:  # food
                    liste_food = line.strip().split(',')
                    finni = True
                i += 1

        if choice == 0:
            res = liste_mob
        elif choice == 1:
            res = liste_obstacle
        else:
            res = liste_food
        return res


class PositionFood(Position):
    def __init__(self):
        super().__init__(1)
        score = MAX_FOOD - len(self.list)

        if score > 0:
            for i in range(score):
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
        super().__init__(0)
        score = MAX_MOB - len(self.list)

        if score > 0:
            for i in range(score):
                finni = False
                while not finni:
                    x = randint(0, MAT_SIZE - 1)
                    y = randint(0, MAT_SIZE - 1)
                    if (x, y) not in self.list:
                        self.list.append((x, y))
                        finni = True

    def getList(self):
        return self.list


class PositionObstacle(Position):
    def __init__(self):
        super().__init__(2)


    def getList(self):
        return self.list


# Matrice
MAT_SIZE = 10

# Food
MAX_FOOD = 7
FPOSITIONS = PositionFood().getList()
FSIGN = ' @ '

# Mob
MAX_MOB = 10
MPOSITION = PositionMob().getList()
MSIGN = ' ' + chr(254) + ' '

# Obstacle
OPOSITION = PositionObstacle().getList()
OSIGN = ' X '

