import re
import string
import nltk
import spacy
import pandas as pd
import numpy as np
import math
from tqdm import tqdm

from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

pd.set_option('display.max_colwidth', 200)

nlp = spacy.load("en_core_web_sm")

# sample text
text = "6 injured in crash this morning." \
       ""
doc = nlp(text)

# print([token.pos_ for token in doc])

# define the pattern

pattern = [{'POS': 'NUM'}, {'POS': 'VERB'}]

# Matcher class object

matcher = Matcher(nlp.vocab)
matcher.add("matching", None, pattern)

matches = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)
