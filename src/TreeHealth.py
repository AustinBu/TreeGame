import math
import random
import pygame


class TreeHealth:
    def __init__(self, imagelist, x):
        self.imagelist = imagelist
        self.image = imagelist[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = imagelist[0][1]
        self.water_state = 'normal'
        self.fertilizer_state = 'normal'
        self.water = 0
        self.fertilizer = 0
        self.WATER_MAX = 1000
        self.FERTILIZER_MAX = 1000
        self.growth = 0
        self.growth_stage = 0
        self.alive = True
        self.deadtime = 0

    def lose_water(self):
        self.water = self.water - math.ceil(self.water * self.water / 100000)

    def lose_fertilizer(self):
        self.fertilizer = self.fertilizer - random.randint(1, 10)

    def add_water(self):
        if self.alive:
            self.water = self.water + 100

    def add_fertilizer(self):
        if self.alive:
            self.fertilizer = self.fertilizer + 150

    def check_water(self):
        if self.water <= 0:
            self.water_state = 'dry'
            if self.alive:
                self.update_stage(3)
                self.deadtime = pygame.time.get_ticks()
            self.alive = False
            self.growth = 0
        elif self.water <= 300:
            self.water_state = 'thirsty'
        elif self.water <= 800:
            self.water_state = 'normal'
        elif self.water <= 1000:
            self.water_state = 'wet'
        elif self.water > self.WATER_MAX:
            self.water_state = 'soggy'

    def check_fertilizer(self):
        if self.fertilizer <= 0:
            self.fertilizer_state = 'starving'
            self.growth = 0
            if self.alive:
                self.update_stage(3)
                self.deadtime = pygame.time.get_ticks()
            self.alive = False
        elif self.fertilizer <= 300:
            self.fertilizer_state = 'hungry'
        elif self.fertilizer <= 800:
            self.fertilizer_state = 'normal'
        elif self.fertilizer <= 1000:
            self.fertilizer_state = 'full'
        elif self.fertilizer > self.FERTILIZER_MAX:
            self.fertilizer_state = 'stuffed'

    def check_growth(self):
        if self.growth_stage == 0 and self.growth > 10:
            self.update_stage(1)
        elif self.growth_stage == 1 and self.growth > 20:
            self.update_stage(1)

    def update_stage(self, x):
        self.growth_stage += x
        self.image = self.imagelist[self.growth_stage][0]
        x = self.rect.x
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = self.imagelist[self.growth_stage][1]

