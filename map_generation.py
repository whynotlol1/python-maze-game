# All the code here was taken from https://github.com/xsafter/map-generator/tree/main
# Feel free to use some parts of this code in your project

from collections import deque
import random


def make_grid(width, height):
    new_grid = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if i == 0 or j == 0 or i == len(new_grid) - 1 or j == len(new_grid[0]) - 1:
                new_grid[i][j] = 1
    return new_grid


def populate_grid(grid, chance):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if random.randint(0, 100) <= chance: 
                grid[i][j] = 1
    return grid


def automata_iteration(grid, min_count, make_pillars):
    new_grid = [row[:] for row in grid]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            count = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if grid[i + k][j + l] == 1:
                        count += 1
            if count >= min_count or (count == 0 and make_pillars == 1):
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0
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
        # find a random empty space, hope it's the biggest cave
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
                    if 0 <= current[0] + k < len(grid) and 0 <= current[1] + l < len(grid[0]):  # If we're not out of bounds
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

    for i in range(iterations):
        grid = automata_iteration(grid, count, 0)

    grid = flood_find_empty(grid, floodTries, goalPercentage)

    return grid