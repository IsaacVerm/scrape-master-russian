from src.get_html import get_html_page, get_html_word
from src.parse_html import parse_urls_words, parse_phrases
from src.write_to_file import write_phrases_to_tsv, write_phrases_header_to_tsv

# define pages with words
page_numbers = list(range(1, 13))

# create phrases file with header but no rows
write_phrases_header_to_tsv()

# scrape
for page_number in page_numbers:
    try:
        html_page = get_html_page(page_number)
        urls_words = parse_urls_words(html_page)
    except:
        pass

    for url_word in urls_words:
        try:
            html_word = get_html_word(url_word)
            phrases = parse_phrases(html_word)
            write_phrases_to_tsv(phrases)
        except:
            print(f"something went wrong with the url {url_word}")
