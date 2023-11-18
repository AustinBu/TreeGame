import math
import random


class Tree:
    def __init__(self, x, y):
        self.size = [x, y]
        self.water_state = 'normal'
        self.nutrient_state = 'normal'
        self.water = 500
        self.nutrients = 500
        self.WATER_MAX = 1000
        self.NUTRIENT_MAX = 1000

    img=''

    def lose_water(self):
        self.water = self.water - math.ceil(self.water * self.water / 100000)

    def lose_nutrients(self):
        self.nutrients = self.nutrients - random.randint(1, 10)

    def add_water(self):
        self.water = self.water + 100

    def add_nutrients(self):
        self.nutrients = self.nutrients + 150

    def check_water(self):
        if self.water <= 0:
            self.water_state = 'dry'
        elif self.water <= 300:
            self.water_state = 'thirsty'
        elif self.water <= 800:
            self.water_state = 'normal'
        elif self.water <= 1000:
            self.water_state = 'wet'
        elif self.water > self.WATER_MAX:
            self.water_state = 'soggy'

    def check_nutrients(self):
        if self.nutrients <= 0:
            self.nutrient_state = 'starving'
        elif self.nutrients <= 300:
            self.nutrient_state = 'hungry'
        elif self.nutrients <= 800:
            self.nutrient_state = 'normal'
        elif self.nutrients <= 1000:
            self.nutrient_state = 'full'
        elif self.nutrients > self.NUTRIENT_MAX:
            self.nutrient_state = 'stuffed'
