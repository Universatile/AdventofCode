# Day 6 of Advent of Code
# Author: Jason Rennie


def redist(banks):
    """Resdistributes the blocks from the largest memory bank to other banks,
    sequentially with one per bank until completely redistributed.
    """
    k = max(banks)
    i = banks.index(k)
    end = len(banks)
    banks[i] = 0
    while k > 0:
        i += 1
        if i == end:
            i = 0
        banks[i] += 1
        k -= 1
    return banks


def count_cycles(banks):
    """Records permutations and checks for the first repeat. Prints number
    of cycles total, and number of cycles between repeats.
    """
    perms = []
    while banks not in perms:
        perms.append(banks)
        banks = redist(list(banks))

    print("The numbers of cycles required to redistribute is:",
          len(perms))
    print("The numbers of cycles between repeats is:",
          len(perms) - perms.index(banks))

file = open("day6.txt", "r")
banks = [int(n) for n in file.read().split()]  # Initial configuration
file.close()

count_cycles(banks)
