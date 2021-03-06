from requests import get

def get_page_numbers():
    return list(range(1, 13))

def get_html_page(page_number):
    print(f"getting html page {page_number}")

    if page_number == 1:
        return get('http://masterrussian.com/vocabulary/most_common_words.htm').content
    else:
        return get(f'http://masterrussian.com/vocabulary/most_common_words_{page_number}.htm').content


def get_html_word(url):
    print(f"getting html for {url}")
    return get(url).content
