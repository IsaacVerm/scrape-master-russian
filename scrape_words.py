from get_html import get_html_page, get_html_word
from parse_html import parse_urls_words, parse_phrases
from write_to_file import write_phrases_to_tsv

# get html page 1
html_page = get_html_page(1)

# parse urls words
urls_words = parse_urls_words(html_page)

# get html first word
html_word = get_html_word(urls_words[0])

# parse phrases first word
phrases = parse_phrases(html_word)

# write phrases to file
write_phrases_to_tsv(phrases)
