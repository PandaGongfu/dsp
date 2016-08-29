#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

# train a Markov text generator using trigram model

from random import random
from bisect import bisect
import sys

punctuation = '.,;:!?"'


def read_file(filename):
    fh = open(filename, 'r')
    words = []
    _ = [words.extend(sentence.split(' ')) for sentence in fh.read().split('\n')]
    words = [word for word in words if len(word)]
    fh.close()
    return words


def train_model(words):
    for k, x in enumerate(words):
        if x[-1] in punctuation:
            words[k] = [x[:-1], x[-1]]
    all_words = []
    _ = [all_words.append(elem) if str == type(elem) else all_words.extend(elem) for elem in words]

    monogram = {}
    for word in all_words:
        monogram.setdefault(word, 0)
        monogram[word] += 1

    bigram = {}
    for k, word in enumerate(all_words[1:]):
        bigram.setdefault((all_words[k], word), 0)
        bigram[(all_words[k], word)] += 1

    trigram = {}
    for k, word in enumerate(all_words[2:]):
        trigram.setdefault((all_words[k], all_words[k+1],word), 0)
        trigram[(all_words[k], all_words[k+1], word)] += 1
    return [monogram, bigram, trigram]


# random assign the next weight based on weights in ngrams
def weighted_choice(ngram, key):
    if len(key):
        filtered = {k: v for k, v in ngram.items() if k[:-1] == key}
    else:
        filtered = ngram

    if not len(filtered):
        return ''
    choices = list(filtered.keys())
    weights = list(filtered.values())

    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)

    x = random() * total
    i = bisect(cum_weights, x)
    if not len(key):
        return choices[i]
    else:
        return choices[i][-1]


def generate_bigram(markov_text, monogram, bigram):
    first = weighted_choice(monogram, ())
    while first in punctuation:
        first = weighted_choice(monogram, ())
    markov_text += ' '
    markov_text += first

    second = weighted_choice(bigram, tuple(first))
    if second not in punctuation:
        markov_text += ' '
    markov_text += second
    return markov_text, (first, second)


# Markov text generator
def generate_txt(ngrams, nwords):
    markov_text = ''
    monogram, bigram, trigram = ngrams

    markov_text, (first, second) = generate_bigram(markov_text, monogram, bigram)
    count_words = 2
    while count_words < nwords:
        third = weighted_choice(trigram, (first, second))
        if not len(third):
            markov_text, (first, second) = generate_bigram(markov_text, monogram, bigram)
            count_words += 2
        else:
            if third not in punctuation:
                markov_text += ' '
            markov_text += third
            first = second
            second = third
            count_words += 1
    return markov_text


def usage():
    print('python markov.py train.txt #words\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        sys.exit(2)

    ngrams = train_model(read_file(sys.argv[1]))
    text = generate_txt(ngrams, int(sys.argv[2]))
    print(text)
