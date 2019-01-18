import pygame

pygame.init()

done = True

gameDisplay = pygame.display.set_mode((800,800))

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(gameDisplay, (255,0,0), (300, 300, 300, 300), 0)