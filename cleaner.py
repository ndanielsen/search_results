#! /usr/bin/env python
"""
Data Cleaning file for Auto_Ensemble 0.2

by Nathan Danielsen
nathanjdanielsen@gmail.com
"""

#### Text cleaning utilities

### Lower
### Remove stop words
### Correct mispellings
### Remove HTML / Markup


import nltk.data
from nltk.tokenize import PunktWordTokenizer



class TextCleaner(object):
	"""
	Takes in an iterable / sequence of multi-sentence text.

	Returns cleaned text as requested.

	Author Note: 
	The goal is to have standardized text cleaning utilities that I can use for 
	any text application with multi-language support.
	
	"""

	def __init__(self, language='english'):

		self.tokenizer = = nltk.data.load(‘tokenizers/punkt/' + language + '.pickle’)
		self.punkt_word_tokenizer = PunktWordTokenizer()
	
	def sentence_tokenize(text):
		self.sentences = tokenizer.tokenize(text)




	def remove_stop(sentence):
		self.punkt_word_tokenizer.tokenize(sentence)





	return text




#### Extract Features

### First Four sentences
### extract nouns
### extract adjectives


#### NLP Analysis

### Compare to see if search ngram is in title or first four sentences
### Use thesarsus of words and swap out for words in ngram
### 







class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		