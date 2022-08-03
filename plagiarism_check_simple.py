# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:40:31 2022

@author: hp
"""

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gensim
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from gensim import Word2Vec
essays=pd.read_csv("essays.csv")
essays.head()
essays.isnull().sum()
essays.drop('cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN')

