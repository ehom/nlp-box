#!/usr/bin/env python3

import nltk
from pprint import pprint as pp

document = "The quick fox jumped over the lazy brown dog."

def separator():
    print("~" * 21)

separator()
print("Text: {}".format(document))

tokens = nltk.word_tokenize(document.lower())

separator()
print("Tokens:")
pp(tokens)
separator()

print("POS Tags:")
tagged = nltk.pos_tag(tokens)
pp(tagged)
separator()

