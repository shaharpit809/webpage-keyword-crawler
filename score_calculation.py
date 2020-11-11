# -*- coding: utf-8 -*-
"""
@author: arpit
"""
from collections import defaultdict
import operator
from utils import TextUtils

t_utils = TextUtils()

class ScoreCalculation():
    def __init__(self):
        """
        Initializing a mapping score for each tag
        and a mapping to maintain score for each keyword
        """
        self.tag_score_mapping = {'title': 20, 
                             'meta': 10,
                             'url': 2,
                             'h1': 6,
                             'h2': 5,
                             'h3': 4,
                             'h4': 3,
                             'h5': 2,
                             'h6': 1,
                             'body': 5
                             }
        
        self.keyword_score_mapping = defaultdict(int)
        
    def unigram(self, words, tag):
        """
        Calculate score of all unigrams
        """
        for i in range(0, len(words)):
            word = words[i]
            self.keyword_score_mapping[word] += self.tag_score_mapping[tag]
            
    def bigram(self, words, tag):
        """
        Calculate score of all bigrams
        """
        for i in range(0, len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            
            final = word_1 + ' ' + word_2
            self.keyword_score_mapping[final] += self.tag_score_mapping[tag] * 1.5
            
    def trigram(self, words, tag):
        """
        Calculate score of all trigrams
        """
        for i in range(0, len(words) - 2):
            word_1 = words[i]
            word_2 = words[i + 1]
            word_3 = words[i + 2]
            
            final = word_1 + ' ' + word_2 + ' ' + word_3
            self.keyword_score_mapping[final] += self.tag_score_mapping[tag] * 2
            
    def assign_score(self, words, tag):
        """
        Assign score of all unigrams, bigrams and trigrams
        """
        self.unigram(words, tag)
        self.bigram(words, tag)
        self.trigram(words, tag)

    def filter_keywords(self):
        """
        Sort keywords by score in descending order
        Select top 30 keywords and remove duplicates
        """
        final_keywords = []

        sorted_keywords = sorted(self.keyword_score_mapping.items(), key=operator.itemgetter(1), reverse = True)
        
        top_keywords = sorted_keywords[: 30]
        
        for i in range(0, len(top_keywords)):
            if self.remove_duplicates(i, top_keywords):
                final_keywords.append(top_keywords[i][0])
        
        return final_keywords
        
    def remove_duplicates(self, index, top_keywords):
        """
        Remove duplicate keywords by checking if they already are a part of other selected keywords
        """
        keyword = top_keywords[index][0].replace(' ', '')
        
        for i in range(0, len(top_keywords)):
            if i != index and keyword in top_keywords[i][0].replace(' ', ''):
                return False
            
        return True
    
    def get_top_keywords(self, html, blacklisted_words):
        """
        Process text of all tags and assig
        """  
        title_words = t_utils.clear_text(html.title_text, blacklisted_words)
        meta_words = t_utils.clear_text(html.meta_text, blacklisted_words)
        url_words = t_utils.clear_text(html.url_text, blacklisted_words)
        h1_words = t_utils.clear_text(html.heading_text[0], blacklisted_words)
        h2_words = t_utils.clear_text(html.heading_text[1], blacklisted_words)
        h3_words = t_utils.clear_text(html.heading_text[2], blacklisted_words)
        h4_words = t_utils.clear_text(html.heading_text[3], blacklisted_words)
        h5_words = t_utils.clear_text(html.heading_text[4], blacklisted_words)
        h6_words = t_utils.clear_text(html.heading_text[5], blacklisted_words)
        body_words = t_utils.clear_text(html.body_text, blacklisted_words)

        self.assign_score(title_words, 'title')
        self.assign_score(meta_words, 'meta')
        self.assign_score(url_words, 'url')
        self.assign_score(h1_words, 'h1')
        self.assign_score(h2_words, 'h2')
        self.assign_score(h3_words, 'h3')
        self.assign_score(h4_words, 'h4')
        self.assign_score(h5_words, 'h5')
        self.assign_score(h6_words, 'h6')
        self.assign_score(body_words, 'body')
        
        return self.filter_keywords()