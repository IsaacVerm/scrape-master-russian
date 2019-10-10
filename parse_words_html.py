import bs4
import re
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


def parse_russian_phrase(word):
    soup = bs4.BeautifulSoup(word, 'html.parser')

    phrases = soup.select('.phrase_plain .first')

    try:
        return list(map(lambda phrase: phrase.text, phrases))
    except:
        pass
