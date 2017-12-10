# Day 2 of Advent of Code
# Author: Jason Rennie


def array_file(file):
    """Converts file to 2D array."""
    f_array = []
    for line in file:
        f_array.append([int(i) for i in line.split()])
    return f_array


def get_checksum(array):
    """The checksum is the sum of the difference between the max and min
    value for each row in the 2D array, which consists of rows of integers.
    """
    checksum = 0
    for row in array:
        checksum += max(row) - min(row)
    return checksum


def get_evensum(array):
    """Each row has two integers which divide evenly (no remainder).
    This function returns the sum of the division of each of these pairs.
    """
    evensum = 0
    for row in array:
        for i in row:
            for j in row:
                if i % j == 0 and i != j:
                    evensum += i//j
    return evensum

file = open("day2.txt", "r")
f_array = array_file(file)
file.close()

print(get_checksum(f_array))
print(get_evensum(f_array))
