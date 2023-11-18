import pygame
import math
import time

from Tree import Tree


pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('TreeGame')

item = 'watercan'
tree = Tree()
#clock
clock = pygame.time.Clock()
delta = 0
fps = 60

def load(imgname):
    return pygame.image.load(imgname).convert_alpha()

#images
treepic=load("tree.png")
watercan = load("watercan.png")
watercan = pygame.transform.scale(watercan, size = (128, 64))
watercan2 = load("watercan2.png")
watercan2 = pygame.transform.scale(watercan2,size = (128, 64))
fertilizer = load("fertilizer.png")
fertilizer = pygame.transform.scale(fertilizer,size = (64, 64))
cloud = load('Clouds.png')
cloudbg = load('CloudsBack.png')

# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = load(img)
        self.image = pygame.transform.scale(self.image, (imgw, imgh))
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc




def fertilize(pos):
    global fertilizer
    for x in range(0, 45, 9):
        screen.blit(pygame.transform.rotate(fertilizer, x), pos)
        pygame.display.flip()
        refresh_screen()
    tree.nutrients += 100


def refresh_screen():
    screen.blit(treepic, (200, 200))

# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
#sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)

tiles = math.ceil(1280/cloud.get_width()) + 1
scroll = 0

LOSE_WATER = pygame.USEREVENT + 1
LOSE_NUTRIENTS = pygame.USEREVENT + 2
pygame.time.set_timer(LOSE_WATER, 1000)
pygame.time.set_timer(LOSE_NUTRIENTS, 1000)

status = True
while status:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
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
                pos = [event.pos[0] - 30, event.pos[1] - 70]
                water(pos)
            elif item == 'fertilizer':
                pos = [event.pos[0] - 20, event.pos[1] - 40]
                fertilize(pos)
        elif event.type == LOSE_WATER:
            tree.lose_water()
        elif event.type == LOSE_NUTRIENTS:
            tree.lose_nutrients()

        all_sprites.draw(screen)
        for i in range(0,tiles):
            screen.blit(cloud,(i * cloud.get_width() + scroll,0))
        scroll -= .1
        if abs(scroll) > cloud.get_width():
            scroll = 0
        refresh_screen()
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
