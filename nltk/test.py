#!/usr/bin/env python3

import sys
import nltk
from pprint import pprint as pp


def separator():
    print("~" * 20)


class NlpDoc:
    def __init__(self, doc):
        self.text = doc
        self.tokens = nltk.word_tokenize(self.text.lower())
        self.tagged = nltk.pos_tag(self.tokens)


separator()
print("Python version is {}".format(sys.version))
print("NLTK version is {}".format(nltk.__version__))

separator()
document = "The quick fox jumped over the lazy brown dog."
print("Text: {}".format(document))

nlp_doc = NlpDoc(document)

separator()
print("Tokens:")
pp(nlp_doc.tokens)
separator()

print("POS Tags:")
pp(nlp_doc.tagged)
separator()
