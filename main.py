import pygame, random
from crash import crash
from functions import end
from constants import *

# main game loop 
def gameMain():
    dodged = 0
    carX = (dispWD - carWD) / 2
    carSpeed = 3
    keys = {'left':False, 'right':False}

    rectX = random.randrange(0, dispWD - 100)
    rectY = -500
    rectSpeed = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key in left:
                    keys['left'] = True
                elif event.key in right:
                    keys['right'] = True
            elif event.type == pygame.KEYUP:
                if event.key in left:
                    keys['left'] = False
                elif event.key in right:
                    keys['right'] = False
                    
        if keys['left']:
            carX -= int(carSpeed)
        if keys['right']:
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

        if rectY > dispHT:
            dodged += 1

            rectX = random.randrange(0, dispWD - 100)
            rectY = -100
            rectSpeed += 1

            carSpeed += 0.4