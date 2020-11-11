# -*- coding: utf-8 -*-
"""
@author: arpit
"""
import re

class ParseHtml():
    def __init__(self):
        """
        Initializing text of all tags
        """
        self.title_text = ''
        self.meta_text = ''
        self.url_text = ''
        self.heading_text = ['','','','','','']
        self.body_text = ''
    
    def get_title_words(self, html_doc):
        """
        Extract text from title tag
        """
        title_words = html_doc.find('title')
        
        return title_words.text
    
    def get_meta_words(self, html_doc):
        """
        Extract text from meta tags with 3 different attributes
        """
        name_attr = ['description', 'keywords', 'title']
        meta_words = ''
        for attr in name_attr:
            data = html_doc.find('meta', {"name" : attr})
            if data != None:                
                meta_words += data.get('content') + ' '
             
        return meta_words
                
    def get_url_words(self, url):
        """
        Extract text from URL given as input
        """
        token_filter = r';|,|-|/'
        url_words = re.split(token_filter, url)
        
        return " ".join(url_words)
    
    def get_heading_words(self, html_doc):
        """
        Extract text from all heading tags
        """
        all_headings = []
        
        all_h1 = html_doc.findAll('h1')
        h1_text = ''
        for h1 in all_h1:
            h1_text += h1.text + ' '
        all_headings.append(h1_text.strip())
        
        all_h2 = html_doc.findAll('h2')
        h2_text = ''
        for h2 in all_h2:
            h2_text += h2.text + ' '
        all_headings.append(h2_text.strip())
            
        all_h3 = html_doc.findAll('h3')
        h3_text = ''
        for h3 in all_h3:
            h3_text += h3.text + ' '
        all_headings.append(h3_text.strip())
    
        all_h4 = html_doc.findAll('h4')
        h4_text = ''
        for h4 in all_h4:
            h4_text += h4.text + ' '
        all_headings.append(h4_text.strip())    
        
        all_h5 = html_doc.findAll('h5')
        h5_text = ''
        for h5 in all_h5:
            h5_text += h5.text + ' '
        all_headings.append(h5_text.strip())
        
        all_h6 = html_doc.findAll('h6')
        h6_text = ''
        for h6 in all_h6:
            h6_text += h6.text + ' '
        all_headings.append(h6_text.strip())    
                
        return all_headings
        
    def get_body_words(self, html_doc):
        """
        Extract text from complete body of webpage
        """
        body = html_doc.find('body')
        
        text = body.find_all(text=True)
        
        output = ''
        blacklisted_tags = [
            '[document]',
            'noscript',
            'header',   
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style'
        ]
        
        for t in text:
            if t.parent.name not in blacklisted_tags:
                output += '{} '.format(t)
                
        return output

    def extract_all_text(self, url, html_doc):
        """
        Get all the required text
        """
        self.title_text = self.get_title_words(html_doc)
        self.meta_text = self.get_meta_words(html_doc)
        self.url_text = self.get_url_words(url)
        self.heading_text = self.get_heading_words(html_doc)
        self.body_text = self.get_body_words(html_doc)