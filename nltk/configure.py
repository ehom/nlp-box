#!/usr/bin/env python3

import nltk

print("Downloading NLTK components")

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# from nltk.book import *
# ^^^^^^^^^^^^^^^^^^^^^^^
# This doesn't work. Instead, download each book as follows.

nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')

nltk.download('tagsets')
