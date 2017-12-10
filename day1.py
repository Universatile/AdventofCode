# Day 1 of Advent of Code
# Author: Jason Rennie


def sum_adjacent(string):
    """Sums all digits which match the next digit in the string."""
    count = 0
    for i in range(len(string)):
        if string[i-1] == string[i]:
            count += int(string[i])
    return count


def sum_halfway(string):
    """Sums all digits which match the digit halfway around the string."""
    count = 0
    for i in range(len(string)):
        if string[i-len(string)//2] == string[i]:
            count += int(string[i])
    return count

file = open("day1.txt", "r")
string = file.read()

print(sum_adjacent(string))
print(sum_halfway(string))

file.close()
