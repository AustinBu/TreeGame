import pygame
import math
import time

from Tree import Tree


pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('TreeGame')

clock = pygame.time.Clock()
item = ''
tree = Tree(300, 300)
tree.img = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), tree.size)
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
        tree.add_water()
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
        tree.add_water()
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
    screen.blit(tree.img, (200, 350))
    pygame.display.flip()


# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
#sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)

tiles = math.ceil(1280/cloud.get_width()) + 1
scroll = 0

def clouds():
    global scroll
    screen.blit(cloud, (cloud.get_width() + scroll+500, 0))
    scroll -= 2
    if abs(scroll) > cloud.get_width()+1300:
        scroll = 0

def clouds():
    global scroll
    screen.blit(cloud, (cloud.get_width() + scroll+500, 0))
    scroll -= 2
    if abs(scroll) > cloud.get_width()+1300:
        scroll = 0

LOSE_WATER = pygame.USEREVENT + 1
LOSE_NUTRIENTS = pygame.USEREVENT + 2
pygame.time.set_timer(LOSE_WATER, 1000)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if item == 'watercan':
                water_pos = [event.pos[0] - 30, event.pos[1] - 70]
                watering = True
            elif item == 'fertilizer':
                fertilize_pos = [event.pos[0] - 20, event.pos[1] - 40]
                fertilizing = True
        elif event.type == LOSE_WATER:
            tree.lose_water()
        elif event.type == LOSE_NUTRIENTS:
            tree.lose_nutrients()
    refresh_screen()


pygame.quit()
