

def get_next_target(page):
    start_link = page.find("<a href=")       # assuming links are tagged with <a href=
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    links = []                               # initializes "links" as empty list
    while True:
        url, endpos = get_next_target(page)
        if url:                              # appends each url to "links"
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def get_source(site):                                   # takes in a url and outputs html source for crawling purposes
    page = 0
    return page


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl(seed):
    tocrawl = [seed]                                    # to-do list for crawler
    crawled = []                                        # output of crawler: list of crawled urls
    while tocrawl:
        url = tocrawl.pop(0)                            # crawls starting from *first* page in list "tocrawl"
        if url not in crawled:                          # ensures that we do not crawl the same site over and over again
            links = get_all_links(get_source(url))      # crawls last page and stores in "links"
            union(tocrawl, links)                       # adds newly found links to "tocrawl" using union method
            crawled.append(url)                         # appends crawled page to "crawled"
    return crawled


# seed page is just some url with links on it
seed_site = "http://webtrain.austincc.edu/~jprasadh/"
print(crawl(seed_site))
