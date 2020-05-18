#!/usr/bin/env python3

import spacy
import sys

nlp = spacy.load("en_core_web_sm")


def separator():
    print('~' * 21)


separator()
print("Python version is {}".format(sys.version))
print("\nspaCy version is {}".format(spacy.__version__))

separator()
doc = nlp("She ate the pizza")

# Predicting Syntactic Dependencies

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

separator()

# Process some text
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

separator()

text = """It’s official: Apple is the first U.S. public company
       to reach a $1 trillion market value"""

# Process the text
doc = nlp(text)

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
