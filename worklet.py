
# Import packages

from urllib.error import HTTPError
import nltk

from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen

good = ["good", "excellent", "great", "positive", "sincerity", "fact", "factual", "genuine", "true", "precision", "precise", "truth", "'truth", "honest", "honest", "accuracy", "principle", "veracity", ]
bad = ["awful", "unacceptable", "gross", "junk", "imperfect", "unfavourable", "rough", "unacceptable",  "unpleasant", "terrible", "abhorrent", "dreadful", "evil", "wicked", "wrong", "corrupt", "hateful", "destructive"]

links_count = 0

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = input("Enter the keyword : ")
temp = query
query = query + " wikipedia"
 
wikilinks = []

try:
    for j in search(query, tld="co.in", num=1, stop=1, pause=1):  # change num and stop to how many links u need
        print(j)
        wikilinks.append(j)
        links_count = links_count + 1
    print(wikilinks)
except HTTPError as e:
    print(e)

num1 = links_count                                     # number of links
nouns = []
from spellchecker import SpellChecker
spell = SpellChecker

for i in range(0,num1):
    
    res = requests.get(wikilinks[i])
    soup = bs(res.text, "html.parser")
    naval_battles = {}
    count = 0
    for link in soup.find_all("a"):
        url = link.get("href", "")
        if "/wiki/" in url and count != 0 and "." not in url and ":" not in url and "_" not in url:
            naval_battles[link.text.strip()] = url                                                       # all hyperlinks are present here
            count = count + 1
           # print(url)
            wikilinks.append("https://en.wikipedia.org" + url)
            links_count = links_count + 1
    
for i in range(0, links_count):
     
    # Specify url of the web page
    source = urlopen(wikilinks[i]).read()
    # Make a soup 
    soup = bs(source,'lxml')
    #print(soup)
    
    text = ''
    for paragraph in soup.find_all('p'):
        text += paragraph.text
        
    #print(text)                      #uncomment to see text
    
   
    
    
    #nltk.download('punkt')
    #nltk.download('averaged_perceptron_tagger')
    
    
    lines = text
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(lines)
    nouns = nouns + [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    #print(len(nouns))
    #print(nouns)


print(len(nouns))

good_count = 0
bad_count = 0

for i in good:
    for j in nouns:
        if(j == i):
            good_count = good_count + 1
    

for i in bad:
    for j in nouns:
        if(j == i):
            bad_count = bad_count + 1

print("Good count = ")
print(good_count)
print("Bad count = ")
print(bad_count)
