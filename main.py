# -*- coding: utf-8 -*-
"""
@author: arpit
"""
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from parse_html import ParseHtml
from score_calculation import ScoreCalculation

def get_html_doc(url):
    """
    Connect to the URL given by the user. 
    If the connection fails, an error will be printed
    Else the webpage is parsed to get its content
    """
    try:
        response = requests.get(url)
        content = response.text
        
        html_doc = BeautifulSoup(content, 'html.parser')
        html_doc.encode('utf-8')
        return html_doc

    except requests.exceptions.RequestException as e:
        print('Failed to establish a connection. Please check the url.')
        sys.exit(1)

def main():
    html = ParseHtml()
    sc = ScoreCalculation()
    
    if(len(sys.argv) != 2 ): 
     	print('Usage : python main.py [url]')
     	sys.exit(1)
    
    url = sys.argv[1]
    
    # Number of keywords extracted from the webpage
    num_keywords = 8
    
    html_doc = get_html_doc(url)
    
    # Get the domain name to remove it from the list of keywords
    domain = urlparse(url).netloc
    blacklisted_words = domain.split('.')
    blacklisted_words.extend(['http', 'https'])
    
    # Extract all the text present in the parsed document
    try:
        html.extract_all_text(url, html_doc)
    except:
        print('Failed to establish a connection. Please check the URL.')
        sys.exit(1)
    
    # Extract top keywords
    result = sc.get_top_keywords(html, blacklisted_words)
    print(" , ".join(result[: num_keywords]))

if __name__ == '__main__':
    main()