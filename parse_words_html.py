import bs4
from functools import reduce


def parse_links_words(list_words):
    soup = bs4.BeautifulSoup(list_words, 'html.parser')

    words = soup.select('.word a')

    try:
        return list(map(lambda x: x.attrs['href'], words))
    except:
        pass


# keep only valid results (sometimes the href is empty)
def clean_links_words(list_words):
    return list(filter(None, list_words))


def flatten_links_words(list_words):
    return reduce(lambda page_a, page_b: page_a + page_b, list_words)
