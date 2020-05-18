#!/usr/bin/env python3

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

# Predicting Syntactic Dependencies

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

print('~' * 20)

# Process some text
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
