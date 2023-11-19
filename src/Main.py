import pygame
import math
import time

from src.TreeHealth import TreeHealth


# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        self.image = pygame.transform.scale(self.image, (imgw, imgh))
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('TreeGame')

clock = pygame.time.Clock()
item = ''
tree_list = []
tree_list.insert(0, TreeHealth(pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (300, 300)), 200, 350))
water_time = 0
watering = False
water_pos = [0, 0]
fertilizer_time = 0
fertilizing = False
fertilize_pos = [0, 0]
watercan = [pygame.transform.scale(pygame.image.load("watercan.png").convert_alpha(), (128, 64)),
            pygame.transform.scale(pygame.image.load("watercan2.png").convert_alpha(), (128, 128))]
fertilizer = [pygame.transform.scale(pygame.image.load("fertilizer.png").convert_alpha(), (64, 64)),
              pygame.transform.scale(pygame.image.load("fertilizer2.png").convert_alpha(), (96, 96))]


def water(pos):
    global water_time, watering
    current_time = pygame.time.get_ticks()
    if current_time - water_time < 750:
        screen.blit(watercan[0], pos)
        pygame.display.flip()
    elif 750 < current_time - water_time < 1250:
        screen.blit(watercan[1], pos)
        pygame.display.flip()
    elif current_time - water_time > 1250:
        pygame.display.flip()
        water_time = current_time
        watering = False
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)


def fertilize(pos):
    global fertilizer_time, fertilizing
    current_time = pygame.time.get_ticks()
    if current_time - fertilizer_time < 750:
        screen.blit(fertilizer[0], pos)
        pygame.display.flip()
    elif 750 < current_time - fertilizer_time < 1250:
        screen.blit(fertilizer[1], pos)
        pygame.display.flip()
    elif current_time - fertilizer_time > 1250:
        pygame.display.flip()
        fertilizer_time = current_time
        fertilizing = False
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)


def refresh_screen():
    clock.tick(30)
    all_sprites.draw(screen)
    clouds()
    if watering:
        water(water_pos)
    if fertilizing:
        fertilize(fertilize_pos)
    for tree in tree_list:
        screen.blit(tree.image, (tree.rect.x, tree.rect.y))
    pygame.display.flip()


# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)
cloud = pygame.image.load('Clouds.png').convert_alpha()
tiles = math.ceil(1280 / cloud.get_width()) + 1
scroll = 0


# tree

def clouds():
    global scroll
    screen.blit(cloud, (cloud.get_width() + scroll + 500, 0))
    scroll -= 2
    if abs(scroll) > cloud.get_width() + 1300:
        scroll = 0


LOSE_NUTRIENTS = pygame.USEREVENT + 1
pygame.time.set_timer(LOSE_NUTRIENTS, 1000)

status = True
while status:
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                item = 'watercan'
            elif event.key == pygame.K_f:
                item = 'fertilizer'
            elif event.key == pygame.K_c:
                for tree in tree_list:
                    print(tree.water)
                    print(tree.fertilizer)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if item == 'watercan':
                water_pos = [event.pos[0] - 30, event.pos[1] - 70]
                watering = True
                for tree in tree_list:
                    if tree.rect.x < event.pos[0] < tree.rect.x + tree.rect[2] and tree.rect.y < event.pos[0] < tree.rect.y + tree.rect[3]:
                        tree.add_water()
            elif item == 'fertilizer':
                fertilize_pos = [event.pos[0] - 20, event.pos[1] - 40]
                fertilizing = True
                for tree in tree_list:
                    if tree.rect.x < event.pos[0] < tree.rect.x + tree.rect[2] and tree.rect.y < event.pos[0] < tree.rect.y + tree.rect[3]:
                        tree.add_fertilizer()
        elif event.type == LOSE_NUTRIENTS:
            for tree in tree_list:
                tree.lose_water()
                tree.lose_fertilizer()
                tree.check_water()
                tree.check_fertilizer()
                if tree.water == 'dry' or tree.water == 'soggy' or tree.fertilizer == 'starving' or tree.fertilizer == 'stuffed':
                    del tree
                elif tree.water != 'thirsty' and tree.fertilizer != 'hungry':
                    tree.growth+=1
                    tree.check_growth()
    refresh_screen()

pygame.quit()
