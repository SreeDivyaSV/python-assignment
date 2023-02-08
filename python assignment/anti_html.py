from bs4 import BeautifulSoup

import requests

def gethtml(url):
    # request web page
    resp = requests.get(url)

    # get the response text. in this case it is HTML
    html = resp.text

    # parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # print the HTML as text
    print(soup.body.get_text().strip())
gethtml("http://example.com/")
