import pygame, random
from crash import crash
from functions import end
from constants import *

# main game loop 
def gameMain(carChange):
    dodged = 0
    carX = (dispWD - carWD) / 2
    carSpeed = 3

    rectX = random.randrange(0, dispWD - 100)
    rectY = -500
    rectSpeed = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key == shelf['controls'][0]:
                    carChange -= int(carSpeed)
                elif event.key == shelf['controls'][1]:
                    carChange += int(carSpeed)
            elif event.type == pygame.KEYUP:
                if event.key == shelf['controls'][0]:
                    carChange += int(carSpeed)
                elif event.key == shelf['controls'][1]:
                    carChange -= int(carSpeed)
                    
        carX += carChange
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
        if carX < 0 - carWD / 2 or carX > dispWD - carWD / 2 or (dispHT - 105 - carHT < rectY < dispHT and carX - 97 < rectX < carX + carWD - 3):
            button, carChange = crash(dodged, carChange / int(carSpeed) * 3)
            if button == crashButton.restart:
                gameMain(carChange)
                return carChange
            elif button == crashButton.home:
                return carChange

        if rectY > dispHT:
            dodged += 1

            rectX = random.randrange(0, dispWD - 100)
            rectY = -100
            rectSpeed += 1

            if int(carSpeed + 0.4) != int(carSpeed):
                if carChange > 0:
                    carChange += 1
                elif carChange < 0:
                    carChange -= 1
            carSpeed += 0.4