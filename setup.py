from cx_Freeze import setup, Executable

options = {
    'packages': ['pygame', 'dbm'],
    'include_files': ['Fonts', 'Images', 'constants.py', 'crash.py', 'functions.py', 'main.py', 'settings.py']
}

setup(
    name='Racecar Dodge',
    description='Use your racecar to dodge as many obstacles as possible!',
    options={'build_exe': options},
    executables=[Executable('start.py', icon='carIcon.ico', targetName='Racecar Dodge.exe')]
)