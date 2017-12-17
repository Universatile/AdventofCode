# Day 11 of Advent of Code
# Author: Jason Rennie
#
# Program Description:
# Input is a set of hex-grid directions (nw, n, ne, se, s, sw).
# The program calculates the distance from the origin after each direction is
# followed. Prints final distance and maximum distance.


def run(directions):
    """Hexagonal map movement using 2D grid coordinates."""
    x = 0
    y = 0
    max_dist = 0

    for i in directions:  # Follow directions for each step
        if i == "nw":
            x -= 1
            y += 1
        elif i == "sw":
            x -= 1
            y -= 1
        elif i == "n":
            y += 2
        elif i == "s":
            y -= 2
        elif i == "ne":
            x += 1
            y += 1
        elif i == "se":
            x += 1
            y -= 1
        distance = get_dist(x, y)
        if max_dist < distance:
            max_dist = distance

    print("The final distance is:", distance)
    print("The maximum distance was:", max_dist)


def get_dist(x, y):
    """Calculates (hexagonal) distance from origin to given position."""
    x, y = abs(x), abs(y)
    return min(x, y) + (max(x, y) - min(x, y))//2

file = open("day11.txt", "r")
directions = [i for i in file.read().rstrip().split(",")]
file.close()

run(directions)
