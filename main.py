import pygame, random
from crash import crash
from functions import end
from constants import *

# main game loop 
def gameMain():
    dodged = 0
    carX = (dispWD - carWD) / 2
    carSpeed = 3
    keys = {'left':[False, False], 'right':[False, False]}

    rectX = random.randrange(0, dispWD - 100)
    rectY = -500
    rectSpeed = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys['left'][0] = True
                elif event.key == pygame.K_a:
                    keys['left'][1] = True
                elif event.key == pygame.K_RIGHT:
                    keys['right'][0] = True
                elif event.key == pygame.K_d:
                    keys['right'][1] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys['left'][0] = False
                elif event.key == pygame.K_a:
                    keys['left'][1] = False
                elif event.key == pygame.K_RIGHT:
                    keys['right'][0] = False
                elif event.key == pygame.K_d:
                    keys['right'][1] = False
                    
        if keys['left'][0] or keys['left'][1]:
            carX -= int(carSpeed)
        if keys['right'][0] or keys['right'][1]:
            carX += int(carSpeed) 
        rectY += rectSpeed
        
        display.fill(white)

        display.blit(car, (carX, dispHT - 5 - carHT))
        pygame.draw.rect(display, shelf['rectColor'], (rectX, rectY, 100, 100))

        display.blit(lobsterS.render('Dodged: ' + str(dodged), True, green), (3, 3))
        record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
        display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))

        pygame.display.update()
        clock.tick(60)

        # when user crashes
        if carX < 0 or carX > dispWD or (dispHT - 105 - carHT < rectY < dispHT and carX - 97 < rectX < carX + carWD - 3):
            button = crash(dodged)
            if button == crashButton.restart:
                gameMain()
                return
            elif button == crashButton.home:
                return

        # when user dodges obstacle
        if rectY > dispHT:
            dodged += 1

            rectX = random.randrange(0, dispWD - 100)
            rectY = -100
            rectSpeed += 1

            carSpeed += 0.4