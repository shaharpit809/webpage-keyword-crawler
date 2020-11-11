# webpage-keyword-crawler

Crawl the given URL and identify relevant topics on that webpage.

## Prerequisites

- Check if `Python 3.x` version is installed or not
	- Check the version using `python --version`
	- If version 2.x is installed or you don't have python, you can download it from [here](https://www.python.org/downloads/)
- Download the required packages using the command `pip`
	- If pip is not installed on your system, you can download it from [here](https://pip.pypa.io/en/stable/installing/)
- Once pip is installed, download the other packages using : 
	- For requests, use `pip install requests`. Read more from [here](https://pypi.org/project/requests/)
	- For beautifulsoup4, use `pip install beautifulsoup4`. Read more from [here](https://pypi.org/project/beautifulsoup4/)
	- For urllib3, use `pip install urllib3`. Read more from [here](https://pypi.org/project/urllib3/)
	- For nltk, use `pip install nltk`. Read more from [here](https://pypi.org/project/nltk/)
	
Requests library is used to connect to the given URL.
BeautifulSoup is used to parse the HTML page.
Urllib is used to get the domain name.
NLTK is a Natural Language Toolkit and is used for Lemmatization.

## Files Overview

- `main.py` : Starting point of the code to find the relevant topics from a webpage
- `parse_html.py` : Takes URL and HTML_Document as input and extracts out text from various HTML tags
- `utils.py` : Provides helper functions to clean the text data and converts it into a readable format by converting it into tokens and lemmatizing it
- `score_calculation.py` : Scores all the unigrams, bigrams and trigrams using a tag based mapping. Extracts top keywords from a webpage using the score generated.

## Execution

- Once all the prerequisites are completed, execute the main.py in the command prompt file by - `python main.py [URL]`
- Please refer the given example - `python main.py "https://www.yelp.com/search?find_desc=Falafel&find_loc=Bloomington%2C+IN&ns=1"`
- Do not forget to provide the URL, else an error will be printed.

- Examples : 
	- `python main.py "https://www.yelp.com/search?find_desc=Falafel&find_loc=Bloomington%2C+IN&ns=1"` : best falafel bloomington , business , order , good , top best falafel , falafel bloomington last , bloomington last update , last update november
	
	- `python main.py "https://www.sephora.com/product/chance-eau-tendre-P258612?icid2=products%20grid:p258612"` : eau de toilette , eau tendre eau , tendre eau de , chance eau tendre , de toilette chanel , fragrance , oz eau de , de toilette spray	
	
	- `python main.py "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"` : introduce indoorsy friend , indoorsy friend outdoors , co op journal , end member comment , camp , friend outdoors co , outdoors co op , hike
	
	- `python main.py "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"` : man behind nsa , behind nsa leak , nsa leak say , leak say safeguard , say safeguard privacy , safeguard privacy liberty , snowden , privacy liberty cnnpolitics

## Steps

- Took the given URL and used requests library to get the complete HTML document
- Parsed the HTML document using BeautifulSoup and extracted text data from tags like - title, meta, heading, body and URL
- Processed the text to special characters and keywords and then generated unigrams, bigrams and trigrams
- Assigned scores to all the cadidate keywords and selected the top 30 candidates
- Filtered the candidates by removing duplicates and finally selected the top 8 keywords to represent the relevant topic on a webpage

## Thought Process

- Preprocessing data
	- Removing stopwords : Removed all the stopwords from the data as they don't have significant importance to understand the context and also to have a better emphasis on important topics of the data
	- Lemmatizing : Converted all the words into their base form to improve frequency of the words and improve performance

- Scoring 
	- Title is the most important tag of a document, which is why I assigned the largest value to it
	- Similarly, assigned different values to different tags depending on the tag
		- Title : 20
		- Meta : 10
		- Body : 5
		- URL : 2
		- H1 : 6
		- H2 : 5
		- H3 : 4
		- H4 : 3
		- H5 : 2
		- H6 : 1
		- Unigram : 1
		- Bigram : 2
		- Trigram : 3

## Possible Improvements

- Few special characters are not included for preprocessing, they can be included to better format the data and generate more possible candidate keywords
- Use Stemming and Lemmatization together to convert more data into their base form and check if performance improves
- Use topic modeling algorithm like LDA to automatically generate keywords to represent various topics in the given data