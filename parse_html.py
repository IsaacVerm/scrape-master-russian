import bs4
import re
from functools import reduce


def parse_urls_words(html_page):
    print("parsing urls words from html page")
    soup = bs4.BeautifulSoup(html_page, 'html.parser')

    words = soup.select('.word a')

    try:
        return list(map(lambda x: x.attrs['href'], words))
    except:
        pass


def parse_phrases(html_word):
    print("parsing phrases from html word")
    soup = bs4.BeautifulSoup(html_word, 'html.parser')

    russian = soup.select('.phrase_plain .first')
    english = soup.select('.phrase_plain .first + li')

    try:
        russian_translations = list(map(lambda element: element.text, russian))
        english_translations = list(map(lambda element: element.text, english))
        return list(zip(russian_translations, english_translations))
    except:
        pass
