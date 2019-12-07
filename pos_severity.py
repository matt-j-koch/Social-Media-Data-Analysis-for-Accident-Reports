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


def severity_tagger(txt):

	nlp = spacy.load("en_core_web_sm")
	doc = nlp(txt)

	# Matcher class object
	matcher = Matcher(nlp.vocab)
	matcher.add("matching", None, [{'LOWER': {'IN': ['no', 'none']}}, {'LOWER': {'IN': ['injuries', 'injured',
																						'hurt', 'harmed', 'damage',
																						'damages', 'damaged']}}],
				[{'POS': 'NUM'}, {'LOWER': {'IN': ['vehicle', 'vehicles', 'car', 'cars', 'truck', 'trucks', 'semi',
												   'semis', 'van', 'vans', 'sedan', 'sedans', 'people', 'injured',
												   'injury', 'injuries', 'killed', 'damaged', 'involved']}}])

	matches = matcher(doc)

	for match_id, start, end in matches:
		span = doc[start:end]
		print(span.text)

	return span.text

