import pygame, shelve
from enum import Enum

pygame.init()

# display values
dispWD = 800
dispHT = 700

# basic colors
white = (255, 255, 255)
red = (175, 0, 0)
green = (124, 252, 0)
blue = (65, 105, 225)

# rect colors
black = (0, 0, 0)
grey = (150, 150, 150)
DKblue = (0, 0, 255)
purple = (75, 0, 130)
DKred = (139, 0, 0)
rectColors = [black, grey, DKblue, purple, DKred]

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
carWD, carHT = car.get_size()

# user data from shelve
shelf = shelve.open('data')
if 'record' not in shelf.keys():
    shelf['record'] = 0
if 'rectColor' not in shelf.keys():
    shelf['rectColor'] = black

# buttons for crash.py
class crashButton(Enum):
    restart = 0
    home = 1