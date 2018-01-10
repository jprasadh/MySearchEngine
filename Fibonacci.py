

# defined recursively
def fibonacci(n):
    if n == 0:
        fib = 0
    elif n == 1:
        fib = 1
    elif n > 1:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
    else:
        raise RuntimeError("Input must be natural number")
    return fib


# defined iteratively
def faster_fibonacci(n):
    if n < 0:
        raise RuntimeError("Input must be natural number")
    current_val = 0
    next_val = 1
    for i in range(0, n):
        current_val, next_val = next_val, current_val + next_val
    return current_val

