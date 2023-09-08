# Feel free to use some parts of this code in your project

# This is basically a configuration file.
# You can change some values here

GAME = {
    "BOUNDS": 700,  # Keep an integer number
    "UNIT_SIZE": 20,  # Keep an integer number less than BOUNDS
    "GAME_SPEED": 20,  # Keep an integer number
    "VERSION": "#0.0.4.2 beta",  # Do not change
    "IS_RUNNING": True,  # Do not change
    "LEVEL": "MAIN-MENU"  # Not used yet. Is needed for the #0.0.5 beta update # Do not change
}

PLAYER = {
    "POSITION": {
        "X": GAME["UNIT_SIZE"],  # Do not change
        "Y": GAME["UNIT_SIZE"]  # Do not change
    },  # Starting position. Starting in the middle of the entrance area
    "SPEED": GAME["UNIT_SIZE"],  # Temporary measure for the collision handler to work  # Do not change
    "IS_RENDERED": True  # Do not change
}

COLORS = {
    "BLACK": (0, 0, 0),  # Only change if you know what you are doing
    "WHITE": (255, 255, 255),  # Only change if you know what you are doing
    "YELLOW": (204, 204, 0),  # Only change if you know what you are doing
    "RED": (250, 50, 0)  # Only change if you know what you are doing
}
