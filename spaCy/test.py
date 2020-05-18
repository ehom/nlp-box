#!/usr/bin/env python3

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

# Predicting Syntactic Dependencies

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
