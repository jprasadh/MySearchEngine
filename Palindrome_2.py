

# defined using recursion
def is_palindrome(word):
    if word == "":
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False

