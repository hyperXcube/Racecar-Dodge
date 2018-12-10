import pygame
from constants import *

# settings page
def settings(carChange):
    back = lobsterS.render('Back', True, black)
    backRect = back.get_rect(topleft = (5, 3))
    rects = {}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carChange -= 4
                elif event.key == pygame.K_RIGHT:
                    carChange += 4
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    carChange += 4
                elif event.key == pygame.K_RIGHT:
                    carChange -= 4
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if backRect.collidepoint(mouse):
                    return carChange
                for color in rects.keys():
                    if rects[color].collidepoint(mouse):
                        shelf['rectColor'] = color

        display.fill(white)

        display.blit(back, backRect)
        display.blit(oswald.render('Change obstacle color:', True, black), (5, 75))

        for i in range(len(rectColors)):
            pos = (dispWD - len(rectColors) * 100) / (len(rectColors) + 1) * (i + 1) + i * 100
            rects[rectColors[i]] = pygame.Rect(pos, 150, 100, 100)
            if shelf['rectColor'] == rectColors[i]:
                pygame.draw.rect(display, green, (pos - 3, 147, 106, 106))
            pygame.draw.rect(display, rectColors[i], (pos, 150, 100, 100))

        pygame.display.update()
        clock.tick(10)