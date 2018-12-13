import pygame
from constants import *

# settings page
def settings(carChange):
    colorRects = {}
    ctrlRects = {}

    back = lobsterS.render('Back', True, black)
    backRect = back.get_rect(topleft = (5, 3))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key == shelf['controls'][0]:
                    carChange -= 3
                elif event.key == shelf['controls'][1]:
                    carChange += 3
            elif event.type == pygame.KEYUP:
                if event.key == shelf['controls'][0]:
                    carChange += 3
                elif event.key == shelf['controls'][1]:
                    carChange -= 3
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if backRect.collidepoint(mouse):
                    return carChange
                for color in colorRects.keys():
                    if colorRects[color].collidepoint(mouse):
                        shelf['rectColor'] = color
                for ctrl in ctrlRects.keys():
                    if ctrlRects[ctrl].collidepoint(mouse):
                        shelf['controls'] = ctrl
                        print(ctrl)

        display.fill(white)

        display.blit(back, backRect),
        display.blit(oswald.render('Change obstacle color:', True, black), (5, 75)),
        display.blit(oswald.render('Change controls:', True, black), (5, 300))    

        for i in range(len(rectColors)):
            pos = (dispWD - len(rectColors) * 100) / (len(rectColors) + 1) * (i + 1) + i * 100
            colorRects[rectColors[i]] = pygame.Rect(pos, 150, 100, 100)
            if shelf['rectColor'] == rectColors[i]:
                pygame.draw.rect(display, green, (pos - 3, 147, 106, 106))
            pygame.draw.rect(display, rectColors[i], (pos, 150, 100, 100))
        pos = 1
        for key in controls.keys():
            if shelf['controls'] == controls[key]:
                text = oswald.render(key, True, green)
            else:
                text = oswald.render(key, True, black)
            rect = text.get_rect(center = (dispWD * pos / (len(controls) + 1), 395))
            ctrlRects[controls[key]] = rect
            display.blit(text, rect)
            pos += 1

        pygame.display.update()
        clock.tick(10)