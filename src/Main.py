import random

import pygame
import math

from pygame import mixer
from TreeHealth import TreeHealth


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
mixer.init()
mixer.Channel(0).play(mixer.Sound("./sound/Relax in the Forest.mp3"), loops=-1)

screen = pygame.display.set_mode((1280, 720))
# counter
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

pygame.display.set_caption('TreeGame')

clock = pygame.time.Clock()
item = ''
tree1_imagelist = [(pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_alive_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_alive_midstage.png")
                                           .convert_alpha(), (300, 400)), 310),
                   (pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_alive_adult.png")
                                           .convert_alpha(), (400, 500)), 320),
                   (pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_dead_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_dead_midstage.png")
                                           .convert_alpha(), (300, 400)), 310),
                   (pygame.transform.scale(pygame.image.load("./Trees/Normal/normal_dead_adult.png")
                                           .convert_alpha(), (400, 500)), 270),
                   'normal']

tree2_imagelist = [(pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/healthy_cherry_blossom_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/CherryB_Alive_midstage.png")
                                           .convert_alpha(), (400, 500)), 240),
                   (pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/CherryB_Alive_Adult.png")
                                           .convert_alpha(), (400, 500)), 210),
                   (pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/dead_cherry_blossom_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/CherryB_Dead_midstage.png")
                                           .convert_alpha(), (400, 500)), 240),
                   (pygame.transform.scale(pygame.image.load("./Trees/CherryBlossom/CherryB_Dead_Adult.png")
                                           .convert_alpha(), (400, 500)), 210),
                   'cherry']

tree3_imagelist = [(pygame.transform.scale(pygame.image.load("./Trees/Birch/birch_normal_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/Birch/birch_alive_midstage.png")
                                           .convert_alpha(), (300, 400)), 310),
                   (pygame.transform.scale(pygame.image.load("./Trees/Birch/BirchAlive.png")
                                           .convert_alpha(), (400, 500)), 300),
                   (pygame.transform.scale(pygame.image.load("./Trees/Birch/birch_dead_sapling.png")
                                           .convert_alpha(), (200, 200)), 500),
                   (pygame.transform.scale(pygame.image.load("./Trees/Birch/birch_dead_midstageORadult.png")
                                           .convert_alpha(), (300, 400)), 310),
                   (pygame.transform.scale(pygame.image.load("./Trees/Birch/birch_dead_adult.png")
                                           .convert_alpha(), (400, 500)), 300),
                   'birch']

tree_spots = [350, 650, 50, 950]
tree_spots_taken = [True, False, False, False]
tree_list = []
tree_list.append(TreeHealth(tree1_imagelist, 350))
water_time = 0
watering = False
water_pos = [0, 0]
fertilizer_time = 0
fertilizing = False
fertilize_pos = [0, 0]
seed_image = pygame.transform.scale(pygame.image.load('seed.png').convert_alpha(), (128, 128))
austintree_image = pygame.transform.scale(pygame.image.load('tree.png').convert_alpha(), (128, 128))
textbox_image = pygame.transform.scale(pygame.image.load('tree_textbox.png').convert_alpha(), (458, 512))
text_list = [("Don't forget to water and fertilize",
              " your trees so that they grow strong",
              " and healthy!"),
             ("Don't forget that your trees need",
              "constant caring to stay alive!"),
             ("Each tree has different monetary",
              "values, but you don't care about",
              "money do you?"),
             ("Money is not the type of green that",
              "will give out oxygen to the world!")]

current_gospel = ''

class Menu:
    def __init__(self, posx, posy):
        self.imagelist = [pygame.transform.scale(pygame.image.load("menu.png").convert_alpha(), (512, 192)),
                          pygame.transform.scale(pygame.image.load("menu_water.png").convert_alpha(), (512, 192)),
                          pygame.transform.scale(pygame.image.load("menu_fertilizer.png").convert_alpha(), (512, 192)),
                          pygame.transform.scale(pygame.image.load("menu_sell.png").convert_alpha(), (512, 192))]
        self.x = posx
        self.y = posy
        self.image = self.imagelist[0]


class Water(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.sprites = [pygame.transform.scale(pygame.image.load('can5.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can4.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can3.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can2.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can1.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can6.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can7.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('can8.png').convert_alpha(), (140, 85))]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posx, posy]
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
        self.sprites = [pygame.transform.scale(pygame.image.load('fert1.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('fert2.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('fert3.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('fert4.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('fert5.png').convert_alpha(), (140, 85)),
                        pygame.transform.scale(pygame.image.load('fert6.png').convert_alpha(), (140, 85))]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posx, posy]
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
tiles = math.ceil(1280 / cloud.get_width()) + 1
scroll = 0
menu = Menu(0, 80)

moving_sprites = pygame.sprite.Group()
watering_can = None
fertilizing_bag = None


def refresh_screen():
    global watering, watering_can, moving_sprites, fertilizing_bag, fertilizing
    clock.tick(30)
    all_sprites.draw(screen)
    clouds()
    for tree in tree_list:
        screen.blit(tree.image, (tree.rect.x, tree.rect.y))
    screen.blit(seed_image, (1050, 90))
    screen.blit(austintree_image, (500, 100))
    screen.blit(textbox_image, (550, -100))
    screen.blit(menu.image, (menu.x, menu.y))
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

    # timer
    font = pygame.font.SysFont('Impact', 60)
    minutes = (pygame.time.get_ticks() - start_ticks) // 60000
    timer_text = font.render('YEARS PASSED: {}'.format(minutes), True, (255, 255, 255))
    screen.blit(timer_text, (20, 20))
    # money counter
    money_text = font.render('$: {}'.format(money), True, (255, 255, 0))
    screen.blit(money_text, (1000, 20))
    font1 = pygame.font.SysFont('Impact', 20)

    a = 0
    for i in current_gospel:
        gospel_text = font1.render('{}'.format(i), True, (0, 0, 0))
        screen.blit(gospel_text, (670, 70+(30*a)))
        a+=1
    pygame.display.flip()


def clouds():
    global scroll
    for i in range(0, tiles):
        screen.blit(cloud, (i * cloud.get_width() + scroll, 0))
    scroll -= 1

    if abs(scroll) > cloud.get_width():
        scroll = 0


# platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0, 0, 1300, 800, 'CloudsBack.png')
# sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sky, platform)
cloud = pygame.image.load('Clouds.png').convert_alpha()
tiles = math.ceil(1280 / cloud.get_width()) + 1
scroll = 0

tiles = math.ceil(1280 / cloud.get_width()) + 1
scroll = 0

LOSE_NUTRIENTS = pygame.USEREVENT + 1
pygame.time.set_timer(LOSE_NUTRIENTS, 1000)
start_ticks = pygame.time.get_ticks()
money = 1000


def check_tree_hitbox(tree, pos):
    return tree.rect.x < pos[0] < tree.rect.x + tree.rect[2] and tree.rect.y - 100 < event.pos[1] \
        < tree.rect.y + tree.rect[3]

def kill_tree(tree):
    tree_spots_taken[tree_spots.index(tree.rect.x)] = False
    tree_list.remove(tree)
    del tree

text = False
text_time = 0
def preach_brother():
    global text
    global current_gospel
    global text_time
    if random.randint(0, 100) == 0:
        if not text:
            text = True
            text_time = pygame.time.get_ticks()
            current_gospel = text_list[random.randint(0, len(text_list)-1)]
        elif pygame.time.get_ticks() - text_time > 10000:
            text = False
            current_gospel = text_list[0]

loss = False
def check_loss():
    if money < 1000 and tree_spots_taken.index(True) == -1:
        loss = True

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
            elif event.key == pygame.K_r and loss == True:
                money += 1000
                tree_list.append(TreeHealth(tree1_imagelist, tree_spots[0]))
            elif event.key == pygame.K_c:
                    for tree in tree_list:
                        print(tree.alive)
                        print(tree.water)
                        print(tree.fertilizer)
                        print(tree.growth)
                        print(tree.growth_stage)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mixer.Channel(1).play(mixer.Sound("./sound/click.wav"))
            if menu.x < event.pos[0] < menu.x + menu.image.get_rect()[2] \
                    and menu.y < event.pos[1] < menu.y + menu.image.get_rect()[3]:
                if menu.x + 48 < event.pos[0] < menu.x + 188:
                    item = 'watercan'
                    menu.image = menu.imagelist[1]
                elif menu.x + 188 < event.pos[0] < menu.x + 328:
                    item = 'fertilizer'
                    menu.image = menu.imagelist[2]
                elif menu.x + 328 < event.pos[0] < menu.x + 468:
                    item = 'sell'
                    menu.image = menu.imagelist[3]
            elif 1050 < event.pos[0] < 1050 + seed_image.get_rect()[2] \
                    and 90 < event.pos[1] < 90 + menu.image.get_rect()[3]:
                if money > 1000 and tree_spots_taken.index(True) != -1:
                    mixer.Channel(5).play(mixer.Sound("./sound/plant.wav"))
                    money -= 1000
                    num = random.randint(0, 100)
                    x = tree_spots_taken.index(False)
                    tree_spots_taken[x] = True
                    if num < 50:
                        tree_list.append(TreeHealth(tree1_imagelist, tree_spots[x]))
                    elif num < 80:
                        tree_list.append(TreeHealth(tree3_imagelist, tree_spots[x]))
                    elif num < 90:
                        tree_list.append(TreeHealth(tree2_imagelist, tree_spots[x]))
            elif item == 'watercan' and not watering:
                mixer.Channel(2).play(mixer.Sound("./sound/water.wav"))
                for tree in tree_list:
                    if check_tree_hitbox(tree, event.pos) and money >= 100:
                        money -= 100
                        tree.add_water()
                water_pos = [event.pos[0] - 30, event.pos[1] - 70]
                watering_can = Water(water_pos[0], water_pos[1])
                moving_sprites.add(watering_can)
                watering = True
            elif item == 'fertilizer' and not fertilizing:
                mixer.Channel(3).play(mixer.Sound("./sound/fertilizer.wav"))
                for tree in tree_list:
                    if check_tree_hitbox(tree, event.pos) and money >= 100:
                        money -= 100
                        tree.add_fertilizer()
                fertilize_pos = [event.pos[0] - 20, event.pos[1] - 40]
                fertilizing_bag = Fertilizer(fertilize_pos[0], fertilize_pos[1])
                moving_sprites.add(fertilizing_bag)
                fertilizing = True
                for tree in tree_list:
                    if check_tree_hitbox(tree, event.pos):
                        tree.add_fertilizer()
            elif item == 'sell':
                for tree in tree_list:
                    print(event.pos, tree.rect.x, tree.rect.y, tree.rect)
                    if check_tree_hitbox(tree, event.pos):
                        mixer.Channel(4).play(mixer.Sound("./sound/sell.wav"))
                        money += tree.get_value()
                        kill_tree(tree)

        elif event.type == LOSE_NUTRIENTS:
            for tree in tree_list:
                tree.lose_water()
                tree.lose_fertilizer()
                tree.check_water()
                tree.check_fertilizer()
                if not tree.alive:
                    if pygame.time.get_ticks() - tree.deadtime > 20000:
                        kill_tree(tree)
                elif tree.water_state != 'thirsty' and tree.fertilizer_state != 'hungry':
                    tree.grow()
                    tree.check_growth()
    check_loss()
    preach_brother()
    refresh_screen()
    clock.tick(60)

pygame.quit()
