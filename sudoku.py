#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

numbers = { str(num) for num in range(1, 10) }

grid = []
for line in args.input.readlines():
    row = []
    for char in line.strip():
        if char in numbers:
            row.append(char)
        else:
            row.append(numbers.copy())
    grid.append(row)

finished = 0
while finished < 9 * 9:
    finished = 0
    for y in range(0, 9):
        for x in range(0, 9):
            if isinstance(grid[y][x], set):
                for i in range(0, 9):
                    if isinstance(grid[y][i], str) and grid[y][i] in grid[y][x]:
                        grid[y][x].remove(grid[y][i])
                for j in range(0, 9):
                    if isinstance(grid[j][x], str) and grid[j][x] in grid[y][x]:
                        grid[y][x].remove(grid[j][x])
                min_x = x // 3 * 3
                min_y = y // 3 * 3
                for j in range(min_y, min_y+3):
                    for i in range(min_x, min_x+3):
                        if isinstance(grid[j][i], str) and grid[j][i] in grid[y][x]:
                            grid[y][x].remove(grid[j][i])
                if len(grid[y][x]) == 1:
                    for value in grid[y][x]:
                        pass
                    grid[y][x] = value
            if isinstance(grid[y][x], str):
                finished += 1

for row in grid:
    for char in row:
        print(char, end="")
    print()
