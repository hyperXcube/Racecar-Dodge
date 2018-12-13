from cx_Freeze import setup, Executable
from os import environ

environ['TCL_LIBRARY'] = r'C:\Users\Shaunak.Warty22\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6'
environ['TK_LIBRARY'] = r'C:\Users\Shaunak.Warty22\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6'

options = {'packages':['pygame', 'dbm'],
           'include_files':['Fonts', 'Images', 'constants.py', 'crash.py', 'functions.py', 'main.py', 'settings.py']}

setup(
    name = 'Racecar Dodge',
    description = 'Use your racecar to dodge obstacles and try to get as many blocks dodged as possible!',
    options = {'build_exe': options},
    executables = [Executable('start.py', icon = 'carIcon.ico', targetName = 'Racecar Dodge.exe')]
)