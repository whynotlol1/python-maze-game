# Feel free to use some parts of this code in your project

# This is basically a configuration file.
# Please, do not change anything in this file

GAME = {
    "BOUNDS": 700,  # Do not change
    "UNIT_SIZE": 20,  # Do not change
    "GAME_SPEED": 20,  # Do not change
    "VERSION": "#0.0.5.1 beta",  # Do not change
    "IS_RUNNING": True,  # Do not change
    "LEVEL": "MAIN-MENU"  # Do not change
}

PLAYER = {
    "POSITION": {
        "X": GAME["UNIT_SIZE"],  # Do not change
        "Y": GAME["UNIT_SIZE"]  # Do not change
    },  # Starting position. Starting in the middle of the entrance area
    "SPEED": GAME["UNIT_SIZE"]  # Temporary measure for the collision handler to work  # Do not change
}

COLORS = {
    "BLACK": (0, 0, 0),  # Do not change
    "WHITE": (255, 255, 255),  # Do not change
    "YELLOW": (204, 204, 0),  # Do not change
    "RED": (250, 50, 0)  # Do not change
}
