from Settings import *


class Mob:
    def __init__(self, position, pv, energy, speed, consumption, scope):
        self.coord = position
        self.health = pv
        self.energy = energy
        self.speed = speed
        self.energy_consumption = consumption
        self.scope = scope

    def get_coord(self):
        return self.coord

    def set_coord(self, new_coord):
        self.coord = new_coord

    def get_healt(self):
        return self.health

    def lose_health(self):
        self.health -= 1

    def get_energy(self):
        return self.energy

    def lose_energy(self):
        self.energy -= 1


class Food:
    def __init__(self, position, energy, is_poison=False):
        self.coord = position
        self.given_energy = energy

    def get_coord(self):
        return self.coord

    def remove_coord(self):
        self.coord = None


class Plateau:
    def __init__(self):
        pass