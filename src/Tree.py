import math
import random

class Tree:
    location = [300, 300]

    water_state = 'normal'
    nutrient_state = 'normal'
    water = 500
    nutrients = 500
    WATER_MAX = 1000
    NUTRIENT_MAX = 1000

    def lose_water(self):
        self.water = self.water - math.ceil(self.water * self.water / 100000)

    def lose_nutrients(self):
        self.nutrients = self.nutrients - random.randint(1, 10)

    def add_water(self):
        self.water = self.water + 100

    def add_nutrients(self):
        self.nutrients = self.nutrients + 150

    def check_water(self):
        if self.water <= 0 :
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
        if self.nutrients <= 0 :
            self.nutrient_state = 'starving'
        elif self.nutrients <= 300:
            self.nutrient_state = 'hungry'
        elif self.nutrients <= 800:
            self.nutrient_state = 'normal'
        elif self.nutrients <= 1000:
            self.nutrient_state = 'full'
        elif self.nutrients > self.NUTRIENT_MAX:
            self.nutrient_state = 'full'
            self.nutrients = self.NUTRIENT_MAX




