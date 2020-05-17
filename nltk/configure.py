#!/usr/bin/env python3

import nltk
nltk.download('punkt')

document = "The quick fox jumped over the lazy brown dog."

print("hello, nltk")

tokens = nltk.word_tokenize(document)

print(tokens)

