import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('TreeGame')

tree = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (128, 128))

screen.fill('cadetblue1')
screen.blit(tree, (200, 200))

pygame.display.flip()
status = True
while status:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()
