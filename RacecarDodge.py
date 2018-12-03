import pygame, shelve, random

pygame.init()

# display values
dispWD = 800
dispHT = 700

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (175, 0, 0)
green = (124, 252, 0)
blue = (65, 105, 225)

# fonts
lobsterS = pygame.font.Font(r'Fonts\Lobster-Regular.ttf', 40)
lobsterL = pygame.font.Font(r'Fonts\Lobster-Regular.ttf', 80)
nosifer = pygame.font.Font(r'Fonts\NosiferCaps-Regular.ttf', 80)
oswald = pygame.font.Font(r'Fonts\Oswald-Regular.ttf', 40)

# display/clock settings
display = pygame.display.set_mode((dispWD, dispHT))
pygame.display.set_caption('Racecar Dodge')
clock = pygame.time.Clock()

# car image settings
car = pygame.image.load(r'Images\racecar.png')
carChange = 0
carWD, carHT = car.get_size()

# user record from shelve
shelf = shelve.open('record')
try:
    _ = shelf['record']
except KeyError:
    shelf['record'] = 0

# ends pygame and program
def end():
    shelf.close()
    pygame.quit()
    quit()

# adds text to center of display
def message(s, font, y, color = black):
    text = font.render(s, True, color)
    display.blit(text, text.get_rect(center = (dispWD / 2, dispHT / 2 + y)))

# adds text with color background to display
def button(s, color, center):
    rect = pygame.Rect(0, 0, 150, 100)
    rect.center = center
    pygame.draw.rect(display, color, rect)

    text = oswald.render(s, True, black)
    display.blit(text, text.get_rect(center = center))

    return rect

# start page
def gameStart():
    display.fill(white)
    message('Racecar Dodge', lobsterL, -75)
    message('By Shaunak Warty', lobsterS, 0)
    message('Press any key to start', lobsterS, 50)
    gear = pygame.image.load(r'Images\gear.png')
    gearRect = gear.get_rect(topright = (dispWD - 3, 3))
    display.blit(gear, gearRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYUP:
                gameMain()
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if gearRect.collidepoint(mouse):
                    settings()

        clock.tick(10)

def settings():
    display.fill(white)
    back = lobsterS.render('Back', True, black)
    backRect = back.get_rect(topleft = (5, 3))
    display.blit(back, backRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type ==  pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                
                if backRect.collidepoint(mouse):
                    gameStart()

# main game loop 
def gameMain():
    dodged = 0
    carX = (dispWD - carWD) / 2
    carSpeed = 4
    global carChange
    rectX = random.randrange(0, dispWD - 100)
    rectY = -500
    rectSpeed = 6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carChange -= int(carSpeed)
                elif event.key == pygame.K_RIGHT:
                    carChange += int(carSpeed)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    carChange += int(carSpeed)
                elif event.key == pygame.K_RIGHT:
                    carChange -= int(carSpeed)
                    
        carX += carChange
        rectY += rectSpeed

        display.fill(white)
        display.blit(car, (carX, dispHT - 5 - carHT))
        pygame.draw.rect(display, black, (rectX, rectY, 100, 100))
        display.blit(lobsterS.render('Dodged: ' + str(dodged), True, green), (3, 3))
        record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
        display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))

        pygame.display.update()
        clock.tick(60)

        # code to run when user crashes
        if carX < 0 - carWD / 2 or carX > dispWD - carWD / 2 or (rectY > dispHT - 105 - carHT and carX - 97 < rectX < carX + carWD - 3):
            if dodged > shelf['record']:
                shelf['record'] = dodged
                message('New Record!!', lobsterL, -50, blue)
                pygame.draw.rect(display, white, (dispWD / 2, 3, dispWD / 2, 43))
                record = lobsterS.render('Record: ' + str(shelf['record']), True, blue)
                display.blit(record, record.get_rect(topright=(dispWD - 3, 3)))
            else:
                message('You Crashed', nosifer, -50, red)

            restartRect = button('Restart', green, (dispWD / 4, dispHT * 3 / 4))
            quitRect = button('Quit', red, (dispWD * 3 / 4, dispHT * 3 / 4))

            pygame.display.update()

            carChange = 0

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse = pygame.mouse.get_pos()
                        if restartRect.collidepoint(mouse):
                            gameMain()
                        elif quitRect.collidepoint(mouse):
                            end()
                    elif event.type == pygame.KEYUP and event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                        gameMain()

                    clock.tick(10)

        if rectY > dispHT:
            rectX = random.randrange(0, dispWD - 100)
            rectY = -100
            dodged += 1
            rectSpeed += 1
            if int(carSpeed + 0.5) != int(carSpeed):
                if carChange > 0:
                    carChange += 1
                elif carChange < 0:
                    carChange -= 1
            carSpeed += 0.5

# function calls
gameStart()