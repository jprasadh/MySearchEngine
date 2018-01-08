# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


def hash_string(keyword, buckets):
    unique_sum = 0
    for char in keyword:
        unique_sum += ord(char)
        unique_sum %= buckets
    return unique_sum


print(hash_string('a', 12))
# >>> 1

print(hash_string('b', 12))
# >>> 2

print(hash_string('a', 13))
# >>> 6

print(hash_string('au', 12))
# >>> 10

print(hash_string('udacity', 12))
# >>> 11
