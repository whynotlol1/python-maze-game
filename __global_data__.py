# Feel free to use some parts of this code in your project

GAME = {
    "BOUNDS": 700,
    "UNIT_SIZE": 20,
    "GAME_SPEED": 20,
    "VERSION": "#0.0.4 beta",
    "IS_RUNNING": True
}

PLAYER = {
    "POSITION": {
        "X": GAME["UNIT_SIZE"],
        "Y": GAME["UNIT_SIZE"]
    },  # Starting position. Starting in the middle of the entrance area
    "SPEED": GAME["UNIT_SIZE"]  # Temporary measure for the collision handler to work
}

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "YELLOW": (204, 204, 0),
    "RED": (250, 50, 0)
}
