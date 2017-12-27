

def factorial(n):
    i = n
    fact = 1
    while i > 0:
        fact = fact * i
        i = i - 1
    return fact


print(factorial(4))
