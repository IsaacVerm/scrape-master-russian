from requests import get


def get_list_words(page_number):
    if page_number == 1:
        return get('http://masterrussian.com/vocabulary/most_common_words.htm').text
    else:
        return get(f'http://masterrussian.com/vocabulary/most_common_words_{page_number}.htm').text


def get_word(word_url):
    get(word_url).text
