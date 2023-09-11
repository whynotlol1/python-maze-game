# Algorithm taken from https://github.com/xsafter/map-generator/tree/main
# Feel free to use some parts of this code in your project

from collections import deque
from game.__global__.__global_data__ import *
import random


def make_grid(width, height):
    new_grid = [[0 for _ in range(height)] for _ in range(width)]
    for i_ in range(len(new_grid)):
        for j in range(len(new_grid[i_])):
            if i_ == 0 or j == 0 or i_ == len(new_grid) - 1 or j == len(new_grid[0]) - 1:
                new_grid[i_][j] = 1
    return new_grid


def populate_grid(grid, chance):
    for i__ in range(len(grid)):
        for j in range(len(grid[0])):
            if random.randint(0, 100) <= chance:
                grid[i__][j] = 1
    return grid


def automata_iteration(grid, min_count, make_pillars):
    new_grid = [row[:] for row in grid]
    for i___ in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            count = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if grid[i___ + k][j + l] == 1:
                        count += 1
            if count >= min_count or (count == 0 and make_pillars == 1):
                new_grid[i___][j] = 1
            else:
                new_grid[i___][j] = 0
    return new_grid


def flood_find_empty(grid, tries, goal):
    times_remade = 0
    percentage = 0

    while times_remade < tries and percentage < goal:
        copy_grid = [row[:] for row in grid]
        open_count = 0
        times_remade += 1
        unvisited = deque([])
        new_grid = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # Find a random empty space, hope it's the biggest cave
        randx = random.randint(0, len(grid) - 1)
        randy = random.randint(0, len(grid[0]) - 1)
        while grid[randx][randy] == 1:
            randx = random.randint(0, len(grid) - 1)
            randy = random.randint(0, len(grid[0]) - 1)
        unvisited.append([randx, randy])
        while len(unvisited) > 0:
            current = unvisited.popleft()
            new_grid[current[0]][current[1]] = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= current[0] + k < len(grid) and 0 <= current[1] + l < len(
                            grid[0]):  # If we're not out of bounds
                        if copy_grid[current[0] + k][current[1] + l] == 0:  # If it's an empty space
                            copy_grid[current[0] + k][current[1] + l] = 2  # Mark visited
                            open_count += 1
                            unvisited.append([current[0] + k, current[1] + l])
        percentage = open_count * 100 / (len(grid) * len(grid[0]))

    return new_grid


def generate(width: int, height: int, iterations: int):
    chance = 40
    count = 5
    floodTries = 5
    goalPercentage = 30  # Above 30% seems to be a good target

    grid = make_grid(width, height)

    grid = populate_grid(grid, chance)

    for _ in range(iterations):
        grid = automata_iteration(grid, count, 0)

    grid = flood_find_empty(grid, floodTries, goalPercentage)

    return grid


def generate_level():
    # Generating the map
    map_generated = False
    game_surface = generate(width=GAME["BOUNDS"], height=GAME["BOUNDS"], iterations=1)
    # Drawing the 2 remaining borders (as the originally generated borders are out of reach for the rendering algorithm)
    # Bottom border
    game_surface[GAME["BOUNDS"] - GAME["UNIT_SIZE"]] = [1 for _ in range(GAME["BOUNDS"])]
    # Right border
    for i in range(0, GAME["BOUNDS"], GAME["UNIT_SIZE"]):
        game_surface[i][GAME["BOUNDS"] - GAME["UNIT_SIZE"]] = 1
    # Generating entrance and exit points
    while not map_generated:
        try:
            # Entrance
            for i in range(3):
                game_surface[i * GAME["UNIT_SIZE"]][i * GAME["UNIT_SIZE"]] = 2
                game_surface[0][i * GAME["UNIT_SIZE"]] = 2
                game_surface[i * GAME["UNIT_SIZE"]][0] = 2
            game_surface[GAME["UNIT_SIZE"]][2 * GAME["UNIT_SIZE"]] = 2
            game_surface[2 * GAME["UNIT_SIZE"]][GAME["UNIT_SIZE"]] = 2
            # Exit
            exit_side = random.choice(["right", "bottom"])  # Choosing the side for the exit to generate on
            match exit_side:
                case "bottom":
                    # Bottom border
                    exit_y = GAME["BOUNDS"] - GAME["UNIT_SIZE"]
                    # Inbetween the middle of the border and the corner
                    exit_x = random.randint(int((GAME["BOUNDS"] / GAME["UNIT_SIZE"] / 2)), int(GAME["BOUNDS"] / GAME["UNIT_SIZE"]) - 1)
                    game_surface[exit_x * GAME["UNIT_SIZE"] + GAME["UNIT_SIZE"]][exit_y] = 3
                    game_surface[exit_x * GAME["UNIT_SIZE"]][exit_y] = 3
                    game_surface[exit_x * GAME["UNIT_SIZE"] - GAME["UNIT_SIZE"]][exit_y] = 3
                case "right":
                    # Right border
                    exit_x = GAME["BOUNDS"] - GAME["UNIT_SIZE"]
                    # Inbetween the middle of the border and the corner
                    exit_y = random.randint(int((GAME["BOUNDS"] / GAME["UNIT_SIZE"] / 2)), int(GAME["BOUNDS"] / GAME["UNIT_SIZE"]) - 1)
                    game_surface[exit_x][exit_y * GAME["UNIT_SIZE"] + GAME["UNIT_SIZE"]] = 3
                    game_surface[exit_x][exit_y * GAME["UNIT_SIZE"]] = 3
                    game_surface[exit_x][exit_y * GAME["UNIT_SIZE"] - GAME["UNIT_SIZE"]] = 3
            map_generated = True
        except IndexError:
            pass

    return game_surface
