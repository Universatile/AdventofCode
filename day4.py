# Day 4 of Advent of Code
# Author: Jason Rennie


def is_anagram(word1, word2):
    for ch in word1:
        if (len(word1) != len(word2) or
                word1.count(ch) != word2.count(ch)):
            return 0
    return 1


def check_passphrase(phrase):
    """Input as a string. Valid if all words in phrase are unique
    and no word is an anagram of another word in the phrase.
    """
    phrase = phrase.split()
    for word1 in phrase:
        for word2 in phrase:
            if (phrase.count(word1) > 1 or
                    word1 != word2 and is_anagram(word1, word2)):
                return 0  # Passphrase not valid
    return 1

file = open("day4.txt", "r")

# Count valid passphrases
count = 0
for line in file:
    count += check_passphrase(line)

print(count)

file.close()
