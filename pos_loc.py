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


def num_patterns(txt):

	nlp = spacy.load("en_core_web_sm")
	doc = nlp(txt)

	# Matcher class object
	matcher = Matcher(nlp.vocab)
	matcher.add("matching", None, [{'POS': 'PROPN'}, {'LOWER': {'IN': ['ave', 'avenue', 'st', 'street',
																	   'rd', 'road', 'dr', 'drive',
																	   'pkwy', 'parkway', 'bend', 'bnd',
																	   'boulevard', 'blvd', 'court', 'ct',
																	   'expressway', 'expy', 'freeway', 'fwy',
																	   'highway', 'hwy', 'junction', 'jct',
																	   'lane', 'ln', 'loop', 'motorway', 'mtwy',
																	   'parkway', 'pkwy', 'point', 'pt', 'ramp',
																	   'turnpike', 'tpke', 'tunnel', 'tunl',
																	   'underpass']}}])

	matches = matcher(doc)

	for match_id, start, end in matches:
		span = doc[start:end]
		# print(span.text)

	return span.text

