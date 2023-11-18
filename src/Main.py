import pygame

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

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('TreeGame')

tree = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (128, 128))

screen.fill('cadetblue1')
screen.blit(tree, (200, 200))

pygame.display.flip()
status = True

#platform code
platform = Platform(0, 650, 1300, 100, 'Tileset.png')
sky = Platform(0,0, 1300,800,'CloudsBack.png')
all_sprites = pygame.sprite.Group()
all_sprites.add(sky)
all_sprites.add(platform)

while status:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
    all_sprites.draw(screen)

pygame.quit()
