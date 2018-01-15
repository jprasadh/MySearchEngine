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


def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best = pages[0]
    for page in pages:
        if ranks[page] > ranks[best]:
            best = page
    return best

