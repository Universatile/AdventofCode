# Day 12 of Advent of Code
# Author: Jason Rennie
#
# Program Description:
# Each "program" (identified by integers) has one or more pipes attached to it,
# which are each attached to another program. Input is a list of programs and
# their pipes. A "group" is a set of programs which are connected by the same
# network of pipes.

import re


def follow_pipes(n, checked):
    """Follows pipes to check which programs are part of the same group."""
    for pipe in pipes[n]:
        if pipe not in checked:
            checked.append(pipe)  # Add checked item to group
            follow_pipes(int(pipe), checked)


def group_size(n):
    """Prints the size of a group that includes 'n'."""
    group = []
    follow_pipes(n, group)
    print(len(group))


def count_groups():
    """Total numbers of groups."""
    groups = 0
    checked = []
    for i in range(len(pipes)):
        if str(i) not in checked:
            groups += 1
            follow_pipes(i, checked)
    print(groups)

# Get list of pipes for each program
file = open("day12.txt", "r")
pipes = [re.split(", |,| ", line.strip())[2:] for line in file]
file.close()

# Size of group including 0
group_size(0)

# Number of groups
count_groups()
