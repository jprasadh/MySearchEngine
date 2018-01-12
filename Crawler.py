

def get_next_target(page):
    start_link = page.find("<a href=")  # assuming links are tagged with <a href=
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []  # initializes "links" as empty list
    while True:
        url, endpos = get_next_target(page)
        if url:  # appends each url to "links"
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def get_source(url):  # takes in a url and outputs html source for crawling purposes
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl(seed):
    import Index
    tocrawl = [seed]  # to-do list for crawler
    crawled = []  # output of crawler: list of crawled urls
    index = {}
    graph = {}    # nodes are urls and edges are links from one url's page to another
    while tocrawl:
        url = tocrawl.pop(0)  # crawls starting from *first* page in list "tocrawl"
        if url not in crawled:  # ensures we don't crawl the same site over and over again
            content = get_source(url)  # stores source of site into "content"
            Index.add_page_to_index(index, url, content)
            outlinks = get_all_links(content)  # crawls last page and stores in "outlinks"
            graph[url] = outlinks
            union(tocrawl, outlinks)  # adds newly found links to "next_depth" using union method
            crawled.append(url)  # appends crawled page to "crawled"
    return index, graph


def compute_ranks(graph):
    d = 0.8            # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0/npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank += d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# seed page is just some url with links on it
seed_site = "https://udacity.github.io/cs101x/urank/"
print(get_source(seed_site))
