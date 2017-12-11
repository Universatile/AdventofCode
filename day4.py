# Day 4 of Advent of Code
# Author: Jason Rennie


def check_passphrase(phrase):
    """Input as a string. Valid if all words in phrase are unique."""
    phrase = phrase.split()
    for word in phrase:
        if phrase.count(word) > 1:  # Passphrase not valid
            return 0
    return 1

file = open("day4.txt", "r")

count = 0
for line in file:
    count += check_passphrase(line)

print(count)

file.close()
