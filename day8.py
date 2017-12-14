# Day 8 of Advent of Code
# Author: Jason Rennie
#
# Description: Input a file containing a list of instructions formatted
# in a particular way (e.g. v inc 523 if t == 6). The program initializes
# all mentioned registers to 0 and performs the instructions on these
# registers.

import operator

ops = {"==": operator.eq, "!=": operator.ne, "<": operator.lt,
       ">": operator.gt, "<=": operator.le, ">=": operator.ge}

file = open("day8.txt", "r")

maxvalue = 0
registers = {}

for line in file:
    arr = line.split()

    # Create registers
    if arr[0] not in registers:
        registers[arr[0]] = 0
    if arr[4] not in registers:
        registers[arr[4]] = 0

    # Perform instructions
    if ops[arr[5]](registers[arr[4]], int(arr[6])):
        if arr[1] == "inc":
            registers[arr[0]] += int(arr[2])
        elif arr[1] == "dec":
            registers[arr[0]] -= int(arr[2])

    # Maximum register value seen thus far
    if max(registers.values()) > maxvalue:
        maxvalue = max(registers.values())

file.close()

print("Final maximum value:", max(registers.values()))
print("Maximum value seen:", maxvalue)
