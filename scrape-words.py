from src.get_html import get_page_numbers, get_html_page
from src.parse_html import parse_words
from src.write_to_file import write_header, write_to_tsv

page_numbers = get_page_numbers()

write_header("words")

for page_number in page_numbers:
    html_page = get_html_page(page_number)
    words = parse_words(html_page)
    write_to_tsv("words", words)
