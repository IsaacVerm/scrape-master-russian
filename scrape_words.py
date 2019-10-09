from get_words_html import get_list_words
from parse_words_html import parse_links_words

list_words = get_list_words(1)

links_words = parse_links_words(list_words)

print(links_words)
