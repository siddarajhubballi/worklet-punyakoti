# run below to codes in terminal
# pip install beautifulsoup4
# pip install google



from spellchecker import SpellChecker
spell = SpellChecker

from urllib.request import urlopen
from urllib.error import HTTPError
import nltk
from bs4 import BeautifulSoup as bs
import requests
from googlesearch import search


import wikipedia


# run below two codes once by uncommenting it
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

negativeWords = ['abrasive', 'apathetic', 'controlling', 'dishonest', 'impatient', 'anxious', 'betrayed', 'disappointed', 'embarrassed', 'jealous', 'abysmal', 'bad', 'callous', 'corrosive', 'damage', 'despicable', 'donâ€™t', 'enraged', 'fail', 'gawky', 'haggard', 'hurt', 'icky', 'insane', 'jealous', 'lose', 'malicious', 'naive', 'objectionable', 'pain', 'questionable', 'reject', 'rude', 'sad', 'sinister', 'stuck', 'tense', 'ugly', 'unsightly', 'vice', 'wary', 'yell', 'adverse', 'banal', 'canâ€™t', 'corrupt', 'damaging', 'detrimental', 'dreadful', 'eroding', 'faulty', 'ghastly', 'hurtful', 'ignorant', 'insidious', 'junky', 'lousy', 'mean', 'nasty', 'noxious', 'odious', 'perturb', 'quirky', 'renege', 'ruthless', 'savage', 'slimy', 'stupid', 'terrible', 'undermine', 'untoward', 'vicious', 'weary', 'yucky', 'alarming', 'barbed', 'clumsy', 'dastardly', 'dirty', 'dreary', 'evil', 'fear', 'grave', 'hard-hearted', 'ignore', 'injure', 'insipid', 'lumpy', 'menacing', 'naughty', 'offensive', 'pessimistic', 'repellant', 'scare', 'smelly', 'substandard', 'terrifying', 'unfair', 'unwanted', 'vile', 'wicked', 'angry', 'belligerent', 'coarse', 'crazy', 'dead', 'disease', 'feeble', 'greed', 'harmful', 'ill', 'injurious', 'messy', 'negate', 'reptilian', 'scary', 'sobbing', 'suspect', 'threatening', 'unfavorable', 'unwelcome', 'villainous', 'woeful', 'annoy', 'bemoan', 'creepy', 'decaying', 'disgusting', 'fight', 'grim', 'hate', 'immature', 'misshapen', 'negative', 'oppressive', 'plain', 'repugnant', 'scream', 'suspicious', 'unhappy', 'unwholesome', 'vindictive', 'worthless', 'anxious', 'cold-hearted', 'criminal', 'deformed', 'disheveled', 'filthy', 'grimace', 'hideous', 'imperfect', 'missing', 'poisonous', 'repulsive', 'severe', 'spiteful', 'unhealthy', 'unwieldy', 'apathy', 'boring', 'collapse', 'cruel', 'deny', 'dishonest', 'foul', 'gross', 'homely', 'impossible', 'misunderstood', 'revenge', 'shocking', 'sticky', 'unjust', 'unwise', 'appalling', 'broken', 'confused', 'cry', 'deplorable', 'dishonorable', 'frighten', 'grotesque', 'horrendous', 'inane', 'moan', 'prejudice', 'revolting', 'shoddy', 'stinky', 'unlucky', 'upset', 'atrocious', 'contrary', 'cutting', 'depressed', 'dismal', 'frightful', 'gruesome', 'horrible', 'inelegant', 'moldy', 'nondescript', 'rocky', 'sick', 'stormy', 'unpleasant', 'awful', 'contradictory', 'deprived', 'distress', 'guilty', 'hostile', 'infernal', 'monstrous', 'nonsense', 'rotten', 'sickening', 'stressful', 'unsatisfactory']
positiveWords = ['abundant', 'accepting', 'accomplished', 'accurate', 'achiever', 'active', 'adaptable', 'adept', 'admirable', 'admired', 'adoptive', 'adorable', 'adventurous', 'affection', 'affectionate', 'affluent', 'agreeable', 'amazing', 'ambitious', 'amusement', 'analytical', 'appealing', 'appreciate', 'articulate', 'artistic', 'assertive', 'astounding', 'astute', 'attentive', 'attractive', 'auspicious', 'authentic', 'awesome', 'balanced', 'beaming', 'beautiful', 'best', 'blessed', 'bliss', 'blithesome', 'bold', 'bright', 'brilliant', 'brisk', 'broad-minded', 'buoyant', 'calm', 'candid', 'capable', 'careful', 'caring', 'cautious', 'centered', 'certain', 'changeable', 'charming', 'cheerful', 'childlike', 'clear', 'clear-thinking', 'clever', 'committed', 'compassionate', 'competent', 'complete', 'confident', 'conscientious', 'conscious', 'consciousness', 'considerate', 'consistent', 'constructive', 'content', 'controversial', 'convenient', 'cooperative', 'courage', 'courageous', 'curious', 'customary', 'daring', 'dazzling', 'delicious', 'delight', 'delightful', 'dependable', 'desirable', 'determined', 'devoted', 'diligent', 'diplomatic', 'direct', 'discerning', 'discover', 'dynamic', 'eager', 'easy going', 'efficient', 'effortless', 'elation', 'elegant', 'eloquent', 'emotional', 'empathetic', 'empathy', 'endless', 'energetic', 'engaging', 'enhancer', 'enormous', 'enterprise', 'enterprising', 'enthusiastic', 'enticing', 'excellent', 'excellent', 'exceptional', 'excitement', 'exciting', 'experienced', 'exquisite', 'fabulous', 'fabulous', 'facilitator', 'fair', 'fair-minded', 'faithful', 'fantastic', 'farewell', 'fascinating', 'fast', 'favorable', 'fine', 'fit', 'flattering', 'flourishing', 'focused', 'forgiving', 'fortuitous', 'fortunate', 'free', 'friendliness', 'friendly', 'fulfilled', 'fun', 'funny', 'generous', 'gentle', 'genuine', 'gifted', 'glad', 'glorious', 'glowing', 'good', 'listener', 'natural', 'good-looking', 'gorgeous', 'graceful', 'gracious', 'grand', 'great', 'great', 'green', 'growing', 'handsome', 'happiness', 'happy', 'hard worker', 'hardworking', 'hardy', 'harmonious', 'healed', 'healthy', 'helpful', 'honest', 'hope', 'hopeful', 'humorous', 'ideal', 'idealistic', 'imaginative', 'impressive', 'incredible', 'incredible', 'independent', 'ineffable', 'informal', 'ingenious', 'initiator', 'innovative', 'insightful', 'inspired', 'intelligent', 'intense', 'interest', 'interested', 'interesting', 'intuitive', 'inventive', 'invincible', 'inviting', 'irresistible', 'joy', 'joyous', 'judicious', 'keen', 'kind', 'knowing', 'knowledgeable', 'leader', 'learning', 'leisurely', 'light-hearted', 'likable', 'limitless', 'literate', 'lively', 'logical', 'lovable', 'love', 'loving', 'loyal', 'lucky', 'luminous']

links_count = 0
all_links_count = 0
wikilinks = []
nouns = []

print("")
query = input("Enter the keyword : ")
temp = query
query = query + " wikipedia"
  
for j in search(query,lang = "en", tld="co.in", num=5, stop=5, pause=2):
    wikilinks.append(j)
    links_count = links_count + 1
    all_links_count = all_links_count + 1

print("Fetching URLs...")
for i in range(0,links_count):
    
    res = requests.get(wikilinks[i])
    soup = bs(res.text, "html.parser")
    hyperLinks = {}
    count = 0

    for link in soup.find_all("a"):
        url = link.get("href", "")
        if "/wiki/" in url and count != 50 and "." not in url and ":" not in url and "_" not in url:
            hyperLinks[link.text.strip()] = url                                                       # all hyperlinks are present here
            count = count + 1
            wikilinks.append("https://en.wikipedia.org" + url)
            all_links_count = all_links_count + 1

print("Total number of URLs fetched = " + str(len(wikilinks)))

for i in range(0, all_links_count):
    source = urlopen(wikilinks[i]).read() 
    soup = bs(source,'lxml')
    
    text = ''
    for paragraph in soup.find_all('p'):
        text += paragraph.text


    lines = text
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(lines)
    nouns = nouns + [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    print(str(i+1)+". Fetching words from " + wikilinks[i])

print("Total number of words fetched = " + str(len(nouns)))

good_count = 0
bad_count = 0

for i in positiveWords:
    for j in nouns:
        if(j == i):
            good_count = good_count + 1
    

for i in negativeWords:
    for j in nouns:
        if(j == i):
            bad_count = bad_count + 1

print("Good count = ")
print(good_count)
print("Bad count = ")
print(bad_count)
print("")

if(abs(good_count - bad_count) < 25):
    print(temp + " is Arbuta : Ethical delimma")
elif(good_count > bad_count):
    print(temp + " is Punyakoti : Good")
else:
    print(temp + " is Bad")