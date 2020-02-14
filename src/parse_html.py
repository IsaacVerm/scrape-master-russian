import bs4
import re
from functools import reduce


def parse_urls_words(html_page):
    print("parsing urls words from html page")
    soup = bs4.BeautifulSoup(html_page, 'html.parser')

    words = soup.select('.word a')

    return list(map(lambda x: x.attrs['href'], words))


def parse_words(html_page):
    print("parsing words from html page")

    soup = bs4.BeautifulSoup(html_page, 'html.parser')

    russian = soup.select('.word')
    english = soup.select('.word + td')

    russian_text = list(map(lambda word: word.text, russian))
    english_text = list(map(lambda word: word.text, english))

    return list(zip(russian_text, english_text))


def parse_phrases(html_word):
    print("parsing phrases from html word")
    soup = bs4.BeautifulSoup(html_word, 'html.parser')

    russian = soup.select('.phrase_plain .first')
    english = soup.select('.phrase_plain .first + li')

    russian_translations = list(map(lambda element: element.text, russian))

    # don't bother to continue if there's a flash warning
    for translation in russian_translations:
        if 'Adobe Flash Player' in translation:
            russian_translations = ""

    # continue if there's no warning
    english_translations = list(map(lambda element: element.text, english))
    return list(zip(russian_translations, english_translations))
