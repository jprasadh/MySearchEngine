

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


def get_source(url):                                   # takes in a url and outputs html source for crawling purposes
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
    except:
        return ""
    return ""


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl(seed, max_pages):
    tocrawl = [seed]                                    # to-do list for crawler
    crawled = []                                        # output of crawler: list of crawled urls
    while tocrawl:
        url = tocrawl.pop(0)                            # crawls starting from *first* page in list "tocrawl"
        if url not in crawled and len(crawled) < max_pages:                          # ensures that we do not crawl the same site over and over again
            links = get_all_links(get_source(url))      # crawls last page and stores in "links"
            union(tocrawl, links)                       # adds newly found links to "tocrawl" using union method
            crawled.append(url)                         # appends crawled page to "crawled"
    return crawled


# seed page is just some url with links on it
seed_site = "http://webtrain.austincc.edu/~jprasadh/"
print(crawl(seed_site, 500))
