import pygame, random
from pygame.sprite import Sprite #? Use for later?
from crash import crash
from pause import pause
from functions import end
from constants import *

#? class Block(Sprite):
#?     def __init__(self, y):
#?         Sprite.__init__(self)

# Main Game loop

def main():
    dodged = 0
    carX = (dispWD - carWD) / 2
    carY = dispHT - 5 - carHT
    carSpeed = 3
    keys = {'left':[False, False], 'right':[False, False], 'up': [False, False], 'down': [False, False]}

    rectX = random.randrange(0, dispWD - 100)
    rectY = -500
    rectSpeed = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                end()
            elif event.type == pygame.KEYDOWN:
                #? Maybe find some way to create a switch statement?
                if event.key == pygame.K_LEFT:
                    keys['left'][0] = True
                elif event.key == pygame.K_a:
                    keys['left'][1] = True
                elif event.key == pygame.K_RIGHT:
                    keys['right'][0] = True
                elif event.key == pygame.K_d:
                    keys['right'][1] = True
                elif event.key == pygame.K_UP:
                    keys['up'][0] = True
                elif event.key == pygame.K_w:
                    keys['up'][1] = True
                elif event.key == pygame.K_DOWN:
                    keys['down'][0] = True
                elif event.key == pygame.K_s:
                    keys['down'][1] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys['left'][0] = False
                elif event.key == pygame.K_a:
                    keys['left'][1] = False
                elif event.key == pygame.K_RIGHT:
                    keys['right'][0] = False
                elif event.key == pygame.K_d:
                    keys['right'][1] = False
                elif event.key == pygame.K_UP:
                    keys['up'][0] = False
                elif event.key == pygame.K_w:
                    keys['up'][1] = False
                elif event.key == pygame.K_DOWN:
                    keys['down'][0] = False
                elif event.key == pygame.K_s:
                    keys['down'][1] = False
                elif event.key == pygame.K_ESCAPE:
                    # Paused
                    btnClicked = pause()
                    if btnClicked == crashButton.restart:
                        main()
                        return
                    elif btnClicked == crashButton.home:
                        return
                    keys = {'left':[False, False], 'right':[False, False], 'up': [False, False], 'down': [False, False]}

        if (keys['left'][0] or keys['left'][1]) and carX > 0:
            carX -= int(carSpeed)
        if (keys['right'][0] or keys['right'][1]) and carX < dispWD - carWD:
            carX += int(carSpeed) 
        if (keys['up'][0] or keys['up'][1]) and carY > 0:
            carY -= int(carSpeed)
        if (keys['down'][0] or keys['down'][1]) and carY < dispHT - carHT:
            carY += int(carSpeed)
        rectY += rectSpeed

        display.fill(white)

        display.blit(car, (carX, carY))
        rect = (rectX, rectY, 100, 100)
        pygame.draw.rect(display, shelf['rectColor'], rect)

        display.blit(lobsterS.render('Dodged: ' + str(dodged), True, green), (3, 3))
        record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
        display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))

        pygame.display.update()
        clock.tick(60)

        # When user crashes
        if car.get_rect(topleft=(carX, carY)).colliderect(rect):
            btnClicked = crash(dodged)
            if btnClicked == crashButton.restart:
                main()
                return
            elif btnClicked == crashButton.home:
                return

        # When user dodges obstacle
        if rectY > dispHT:
            dodged += 1

            rectX = random.randrange(0, dispWD - 100)
            rectY = -100
            rectSpeed += 1

            carSpeed += 0.4