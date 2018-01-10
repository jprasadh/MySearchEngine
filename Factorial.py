

# non-recursive definition of factorial
def factorial_old(n):
    i = n
    fact = 1
    while i > 0:
        fact = fact * i
        i = i - 1
    return fact


# new definition using recursion
def factorial(n):
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n - 1)
    return fact

