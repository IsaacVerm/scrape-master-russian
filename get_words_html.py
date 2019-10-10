from requests import get


def get_list_words(page_number):
    print(f"getting words page {page_number}")

    if page_number == 1:
        return get('http://masterrussian.com/vocabulary/most_common_words.htm').text
    else:
        return get(f'http://masterrussian.com/vocabulary/most_common_words_{page_number}.htm').text


def get_word(word_url):
    print(f"getting word for url {word_url}")
    try:
        return get(word_url).text
    except:
        print(f"{word_url} is fishy")
        pass
