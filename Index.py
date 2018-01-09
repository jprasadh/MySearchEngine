index = {}


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        # not found, create new entry
        index[keyword] = [url]


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

