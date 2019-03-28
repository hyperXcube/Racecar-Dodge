import pygame, random
from crash import crash
from pause import pause
from functions import end
from constants import *

# Main Game loop
# Todo: maybe make car move up/down

def main():
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
                elif event.key == pygame.K_ESCAPE:
                    # Paused
                    btnClicked = pause()
                    if btnClicked == crashButton.restart:
                        main()
                        return
                    elif btnClicked == crashButton.home:
                        return
                    keys = {'left':[False, False], 'right':[False, False]}

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

        # When user crashes
        if carX < -10 or carX > dispWD - carWD + 10 or (dispHT - 105 - carHT < rectY < dispHT and carX - 97 < rectX < carX + carWD - 3):
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