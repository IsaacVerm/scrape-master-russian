from get_words_html import get_list_words, get_word
from parse_words_html import parse_links_words, clean_links_words, flatten_links_words, parse_russian_phrase

# get the htmls of all word lists
page_numbers = list(range(8, 9))

list_words = list(map(lambda x: get_list_words(x), page_numbers))

# parse the links for all words
links_words = list(map(lambda x: parse_links_words(x), list_words))

# clean and flatten
links_words = flatten_links_words(clean_links_words(links_words))

# get the htmls of all words
words = list(map(lambda url: get_word(url), links_words))

# parse example phrases
russian_phrases = list(map(lambda word: parse_russian_phrase(word), words))
print(russian_phrases)
