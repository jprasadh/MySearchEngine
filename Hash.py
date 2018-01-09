

def find_entry(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None


def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = find_entry(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])


def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    entry = find_entry(bucket, key)
    if entry:
        return find_entry(bucket, key)[1]
    else:
        return None


def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table


def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size


def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

