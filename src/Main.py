import pygame
import time

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


tree = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (300, 300))

item = 'watercan'
tree = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (128, 128))
watercan = pygame.transform.scale(pygame.image.load("watercan.png").convert_alpha(), (128, 64))
fertilizer = pygame.transform.scale(pygame.image.load("fertilizer.png").convert_alpha(), (64, 64))


screen.fill('cadetblue1')

pygame.display.flip()
status = True


def water(pos):
    for x in range(0, 45, 5):
        water_can = pygame.transform.rotate(watercan, x)
        screen.blit(water_can, pos)
        pygame.display.flip()
        time.sleep(0.1)
        refresh_screen()
    screen.blit(pygame.transform.scale(pygame.image.load("watercan2.png").convert_alpha(), (128, 128)), pos)
    pygame.display.flip()
    time.sleep(0.5)
    refresh_screen()

def fertilize(pos):
    for x in range(0, 45, 5):
        screen.blit(pygame.transform.rotate(fertilizer, x), pos)
        pygame.display.flip()
        time.sleep(0.1)
        refresh_screen()

def refresh_screen():
    screen.fill('cadetblue1')
    screen.blit(tree, (200, 200))
    pygame.display.flip()


#platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0,0, 1300,800,'CloudsBack.png')
all_sprites = pygame.sprite.Group()
all_sprites.add(sky,platform)
cloud = pygame.image.load('Clouds.png').convert_alpha()
#tree

while status:
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
                pos = [event.pos[0]-30, event.pos[1]-70]
                water(pos)
            elif item == 'fertilizer':
                pos = [event.pos[0]-20, event.pos[1]-40]
                fertilize(pos)
            pygame.event.clear()
    all_sprites.draw(screen)
    screen.blit(cloud,(0,0))
    screen.blit(tree, (200, 200))
    pygame.display.update()

pygame.quit()
