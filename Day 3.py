# tests if word is a palindrome: outputs 0 if palindrome, -1 otherwise


def pal_test(word):
    # word can be any string
    reverse = word[::-1]
    is_palindrome = word.find(reverse)
    return is_palindrome


print(pal_test("madam"))


def find_second(source, target):
    first = source.find(target)
    second = source.find(target, first + 1)
    return second


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))
