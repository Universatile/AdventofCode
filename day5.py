# Day 5 of Advent of Code
# Author: Jason Rennie


def moves_to_exit(maze, part):
    """Jump puzzle solver. Counts how many moves it takes to exit maze.
    - Change index by the value stored in that index's location in the maze.
    - Increment this value by 1 after each jump.
    - Increment by -1 if doing Part 2 and value >= 3.
    """
    size = len(maze)
    i = 0
    count = 0
    while i < size:
        n = i
        i += maze[i]
        if part == 2 and maze[n] > 2:
            maze[n] -= 1
        else:
            maze[n] += 1
        count += 1
    return(count)

file = open("day5.txt", "r")
maze = [int(n) for n in file.read().split()]
file.close()

print(moves_to_exit(maze, 1))
print(moves_to_exit(maze, 2))
