import bs4


def parse_links_words(list_words):
    soup = bs4.BeautifulSoup(list_words, 'html.parser')

    words = soup.select('.word a')

    links_words = list(map(lambda x: x.attrs['href'], words))

    return links_words
