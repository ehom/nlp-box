#!/usr/bin/env python3

import sys
import nltk
from pprint import pprint as pp


def separator():
    print("~" * 20)


separator()
print("Python version is {}".format(sys.version))
print("NLTK version is {}".format(nltk.__version__))

separator()
document = "The quick fox jumped over the lazy brown dog."
print("Text: {}".format(document))


separator()
tokens = nltk.word_tokenize(document.lower())
print("Tokens:")
pp(tokens)
separator()

print("POS Tags:")
tagged = nltk.pos_tag(tokens)
pp(tagged)
separator()
