

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


# full content of web page as a string
webpage = """   <html>
                <head>
                <title>hyperlinks</title>
                </head>
                <body bgcolor="#808000">
                
                <h2><font color="DAA520">Hyperlinks</font></h2>
                
                <br><br>
                
                
                <a href="headingstags.html">Find Heading Tags</a>
                <br><br>
                
                <a href="texttags.html">Find Text Tags</a>
                <br><br>
                <a href="http://www.lego.com">Find Lego.com</a>
                <br><br>
                <a href="http://www.autotrader.com">Find Autotrader.com</a>
                <br><br>
                <a href="listtagsa.html">Find List Tags</a>
                <br><br>
                <a href="tables.html">Find Tables</a>
                <br><br>
                <a href="http://www.google.com">
                <img src="images/textbox.bmp"
                     alt="textbox"
                          width="200"
                          height="285" />
                <img src="images/ferrari.jpg"
                     alt="Ferrari" />
                <img src="images/alien.jpg"
                     alt="Bionicle Krika" />
                <img src="images/cookie.jpg"
                     alt="Krika's Cookie"  
                          width="100"
                          height="100"/>
                </a>
                <a href="http://indianajones.lego.com/en-US/default.aspx">
                <img src="images/ferreri origonal.jpg"
                     alt="Ferrari" />
                
                </a>
                <img src="images/prius.jpg"
                     alt="Toyota Prius" />
                <img src="images/smart for two.jpg"
                     alt="Smart Fortwo" />
                <img src="images/jeep.jpg"
                     alt="Jeep Wrangler" />
                <img src="images/dreamcar.jpg"
                     alt="Lambourghini Diablo" />
                
                <img src="images/car.jpg"
                     alt="Ford Mustang" />
                <img src="images/truck.jpg"
                     alt="Ford Ranger" />
                <img src="images/jeepa.jpg"
                     alt="Hummer H2" />
                <img src="images/van.jpg"
                     alt="Honda Odyssy" />
                <img src="images/logo.png"
                     alt="Lego Logo" 
                          width="200"
                          height="200"/>
                <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                <a href="C:\Documents and Settings\student.CE\Desktop\HTML -Kids4\hyperlinks.html">Go To Top Of Page</a>
                </body>
                </html>
        """

print(get_all_links(webpage))
