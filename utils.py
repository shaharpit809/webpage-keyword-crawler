# -*- coding: utf-8 -*-
"""
@author: arpit
"""

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

class TextUtils():
    def __init__(self):
        """
        Initializing WordNetLemmatizer
        """        
        self.wordnet_lemmatizer = WordNetLemmatizer()
    
    def parse_text(self, text):
        """
        Parse text and remove special characters
        """
        text = text.lower()
        token_filters= "[!#%&$+.:;,-<=>?@[\\]^_`{|}~\t\n\"]"
        text = re.sub(token_filters, ' ', text)
        return text
    
    def lemmatize(self, w):
        """
        Lemmatize word given as input and converted into verb
        """
        return self.wordnet_lemmatizer.lemmatize(w, pos="v")
    
    def clear_text(self, text, blacklisted_words):
        """
        Process text by tokenizing, removing both stopwords and blacklisted words
        """
        text = self.parse_text(text)
        text = text.split(' ')
        final_words = []
        for word in text:
            word = self.lemmatize(word)
            if len(word) > 1 and word not in stopwords.words('english') and word not in blacklisted_words:
                final_words.append(word)
                
        return final_words