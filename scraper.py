import requests
from bs4 import BeautifulSoup

corpus = open("corpus.txt", "a", encoding="utf-8")


def load_url(url_to_load, find_links):
    # send a GET request to the URL and get the HTML content
    html_content = requests.get(url_to_load).text

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # extract the header and paragraph elements from the parsed HTML
    paragraph_elements = soup.find_all("p")
    link_elements = soup.find_all("a")

    # print the header and paragraph text
    for element in paragraph_elements:
        corpus.write(element.text.strip() + "\n\n")

    if find_links:
        for element in link_elements:
            if element.attrs["href"].startswith("https://"):
                load_url(element.attrs["href"], False)
            elif element.attrs["href"].startswith("/wiki"):
                load_url("https://en.wikipedia.org" + element.attrs["href"], False)


# specify the Wikipedia article URL to scrape
print("Input an URL: ", end="")

url = input()

load_url(url, True)


