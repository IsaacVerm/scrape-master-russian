# Scrape master Russian

## Setup

Create Python3 [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```
python3 -m venv venv
```

Activate the virtual environment just created:

```
source venv/bin/activate
```

Install libraries specified in `requirements.txt`:

```
pip install -r requirements.txt
```

## Scraping

Scraping files are available in scrape folder. Run them using:

```
python {file}.py
```

## Exploring the data

Printing a Russian phrase (`-f2`) on a specific line (for example line 5 is `NR==5`):

```
cut -f2 phrases.tsv | awk 'NR==5'
```

Its English translation:

```
cut -f1 phrases.tsv | awk 'NR==5'
```

Printing the entire file:

```
cat phrases.tsv
```

## Why the most common words

[Master Russian](http://masterrussian.com/vocabulary/most_common_words.htm) has a list of the 1000 most common words in Russian. According to [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law) _the frequency of any word is inversely proportional to its rank in the frequency table_. So by learning the most common words we should learn the most.

## Logic

### Types of pages

The Master Russian site consists of 2 types of pages:

- words
- phrases

The word pages contain:

- rank
- Russian word
- English translation
- type

Each word page contains links to the example phrases. We only focus on the Russian word and its English translation.

The phrases pages contain several example phrases for each word.

### Order of execution

The scraping for words is the easiest:

```
- get html page 1
    - parse word and translation
    - write word with translation to file
- get html page 2
    ...
```

The scraping for phrases is a bit more involved:

```
- get html page 1
    - parse urls words
        - get html first word
            - parse phrases first word
            - write phrases first word to file
        - get html second word
            ...
- get html page 2
    ...
```

The scraping of phrases overlaps for a large part with the scraping of words so we can reuse the same functions.

The code for both words and phrases is divided into the following parts:

- get html
- parse html
- write csv

The approach is not to first get all the htmls, then parse, etc... but to write to file as soon as possible.

## Issues

### Parsing the phrases

Getting the Russian part is [easy](http://masterrussian.com/vocabulary/god_year.htm) because it has a class `first`. However the translation can be either just a plain English translation or a plain English translation together with a literal English translation. These translations are just `li` elements without any class making it difficult to single them out with `css` selectors. To keep these simple we just keep the plain translation (you can figure out the literal translation easily yourself).

### Commas in output

Since phrases can already contain commas using commas as separators in the data is not that handy. So instead of a csv I'll use a tsv. This has the added benefit of not having to specify a delimiter when going through the file with `cut`.

### Flash warning

Some words have voice recordings. However, they use Flash so there's an alert. This messes with the css selectors used. So at the moment those are filtered out.

### Unexpected parsing errors

Parsing errors could happen in lots of unpredictable ways so I just decide to use `try...catch` and not handle the exception.

## Further improvements

- make parsing class
  - initialize BeautifulSoup just once
- better names in anonymous functions
- remove imports no longer used
  - reduce in parse