

def hashtable_get_bucket(htable, keyword):
    bucket = hash_string(keyword, len(htable))
    return htable[bucket]


def hash_string(keyword, buckets):
    unique_sum = 0
    for char in keyword:
        unique_sum += ord(char)
        unique_sum %= buckets
    return unique_sum


def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

