# Scrape master Russian

## Running the code

## Why the most common words

[Master Russian](http://masterrussian.com/vocabulary/most_common_words.htm) has a list of the 1000 most common words in Russian. According to [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law) _the frequency of any word is inversely proportional to its rank in the frequency table_. So by learning the most common words we should learn the most.

## How to scrape

The words are divided in pages of unequal length. Each page contains the links to individual words. Each word contains example phrases.

So this is the order of execution:

```
- get html page 1
    - parse word urls
        - get html first word
            - parse phrases first word
            - write phrases first word to file
        - get html second word
            ...
- get html page 2
    ...
```
