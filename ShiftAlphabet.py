# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.


def shift(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = alphabet.find(letter)
    if pos == 25:
        return alphabet[0]
    else:
        return alphabet[pos + 1]


def shift_n_letters(letter, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = alphabet.find(letter)
    new = pos + n
    return alphabet[new % len(alphabet)]


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(phrase, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_list = []
    for char in phrase:
        if char in alphabet:
            char_list.append(shift_n_letters(char, n))
        else:
            char_list.append(char)
    return "".join(char_list)

