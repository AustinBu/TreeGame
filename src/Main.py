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

watering = False
class Water(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.sprites = [pygame.transform.scale(pygame.image.load('can5.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('can4.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('can3.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('can2.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('can1.png').convert_alpha(),(140, 85))]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posx,posy]
        self.animating = True
        self.done_animating = False
    
    def update(self):
        if self.animating:
            self.current_sprite += 0.5  
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = len(self.sprites) - 1  
                self.animating = False 
                self.done_animating = True
            
            self.image = self.sprites[int(self.current_sprite)]

fertilizing = False
class Fertilizer(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.sprites = [pygame.transform.scale(pygame.image.load('fert1.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('fert2.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('fert3.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('fert4.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('fert5.png').convert_alpha(),(140, 85)),
        pygame.transform.scale(pygame.image.load('fert6.png').convert_alpha(),(140, 85))]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posx,posy]
        self.animating = True
        self.done_animating = False
    
    def update(self):
        if self.animating:
            self.current_sprite += 0.5  
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = len(self.sprites) - 1  
                self.animating = False 
                self.done_animating = True
            
            self.image = self.sprites[int(self.current_sprite)]
            
# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)
cloud = pygame.image.load('Clouds.png').convert_alpha()
tiles = math.ceil(1280/cloud.get_width()) + 1
scroll = 0

moving_sprites = pygame.sprite.Group()
watering_can = None
fertilizing_bag = None

def refresh_screen():
    global watering,watering_can,moving_sprites,fertilizing_bag,fertilizing
    clock.tick(30)
    all_sprites.draw(screen)
    clouds()
    moving_sprites.update()
    moving_sprites.draw(screen)

    if watering_can and watering_can.done_animating:
        moving_sprites.remove(watering_can)
        watering_can = None  # Reset watering_can
        watering = False

    if fertilizing_bag and fertilizing_bag.done_animating:
        moving_sprites.remove(fertilizing_bag)
        fertilizing_bag = None  # Reset fertilizing bag
        fertilizing = False

    for tree in tree_list:
        screen.blit(tree.image, (tree.rect.x, tree.rect.y))
    pygame.display.flip()


def clouds():
    global scroll
    for i in range(0,tiles):
        screen.blit(cloud, (i * cloud.get_width() + scroll, 0))
    scroll -= 1
    if abs(scroll) > cloud.get_width() :

# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
#sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)
cloud = pygame.image.load('Clouds.png').convert_alpha()
tiles = math.ceil(1280 / cloud.get_width()) + 1
scroll = 0


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if item == 'watercan' and not watering:
                water_pos = [event.pos[0] - 30, event.pos[1] - 70]
                watering_can = Water(water_pos[0], water_pos[1])
                moving_sprites.add(watering_can)
                watering = True
            elif item == 'fertilizer' and not fertilizing:
                for tree in tree_list:
                    if tree.rect.x < event.pos[0] < tree.rect.x + tree.rect[2] and tree.rect.y < event.pos[0] < tree.rect.y + tree.rect[3]:
                        tree.add_water()

                fertilize_pos = [event.pos[0] - 20, event.pos[1] - 40]
                fertilizing_bag = Fertilizer(fertilize_pos[0],fertilize_pos[1])
                moving_sprites.add(fertilizing_bag)
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
    clock.tick(60)

pygame.quit()

