from get_words_html import get_list_words
from parse_words_html import parse_links_words

# get the htmls of all word lists
page_numbers = list(range(1, 3))

list_words = list(map(lambda x: get_list_words(x), page_numbers))

# parse the links for all words
links_words = list(map(lambda x: parse_links_words(x), list_words))
print(links_words)

# get the htmls of all words

# parse meaning, rank, example sentences and idioms
