#input--remove punctuation
import re
import string
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet as wn
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from googletrans import Translator
from textblob import TextBlob

from Organize_Names import word_ID,Corpus_Combo


#inp_words = input('')
def remove_punctuation(word):
    punctuation='!"#$%\'()*+,-/:;<=>?@[\\]^`{|}~'''
    remove_punct = re.sub('[%s]' % re.escape(punctuation), '',str(word))
    return(remove_punct)
    
def tokenize_input(word): 
    tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)#https://www.nltk.org/api/nltk.tokenize.html
    return(tknzr.tokenize(word))

def fuzzy_search(word,corpus):
    answers=[]
    answer=[]
    RATIO=[]
    sim_result=[]
    for w in word:
        RATIO=[process.extract(w,corpus,limit=50,scorer=fuzz.ratio)]
        sim_result=[r[0] for r in RATIO]
        answer = [i[0]for i in sim_result]
        answers.append(answer)
    
    ans=[]
    for a in answers:
        for i in a:
            ans.append(i)
    return ans

#OPTIONAL 
def remove_stemmer(wordlst):
    stemmers=[]
    for i in range(len(word_ID(wordlst))):
        if word_ID(wordlst)[i]=='n':
            stemmer = SnowballStemmer("english", ignore_stopwords=True)#https://www.nltk.org/howto/stem.html
            stemmers.append(stemmer.stem(wordlst[i]))
        else:
            stemmers.append(wordlst[i])
    return(stemmers)

def fuzzy_search(word,aimlist):
    RATIO=[]
    sim_result=[]
    answer=[]
    for w in word:   
        RATIO=[process.extract(w,aimlist,limit=50,scorer=fuzz.ratio)]
    
    sim_result=[r[0] for r in RATIO]
    answer = [i[0]for i in sim_result]
    return answer

def input_processing(translate, input_word, corpus):
    #TRANSLATE
    try:
        translate =='Yes'or'yes'
        language =TextBlob(input_word)
        orilan =language.detect_language()
        if(orilan !='en'):
            translator = Translator()
            result = translator.translate(input_word,src = orilan, dest = 'en') #翻译掉
            input_word=(f'{result.text}')
    except:
        input_word = input_word
        
    no_punctuation = remove_punctuation(input_word)
    tokenize = tokenize_input(no_punctuation)
    #no_stemmer = remove_stemmer(tokenize)
    fuzzy_search_result = fuzzy_search(tokenize,corpus)
    for i in fuzzy_search_result:
        return i

def standard_sector(name):
    nn = name.lower()
    N = nn.capitalize() 
    return ('Sector_'+N)
def standard_owner(name):
    nn = name.lower()
    N = nn.capitalize() 
    return ('Owner_'+N)

'''Corpus= Corpus_Combo(r'C:\Users\DELL\Desktop\RoomName','Sheet1')
noun_corpus = Corpus['noun_n']
all_corpus=[]
for k,v in Corpus.items():
    for i in v:
        all_corpus.append(i)

print('need translation or not ? --yes or no ')
translate=input('')
print('input function_words: ')
INPUT_funct = input('') 
input_function=input_processing(translate,INPUT_funct,noun_corpus)
print('input description_words: ')
INPUT_descri = input('')
input_description = input_processing(translate,INPUT_descri,all_corpus)
print('input Ownership: ')
INPUT_owner = input('')
input_ownership = standard_owner(INPUT_owner)
print('input Sector: ')
INPUT_sector = input('')
input_sector = standard_sector(INPUT_sector)

print('--------------STANDARLIZED CLASSIFICATION------------------------------')
print('Description_'+input_description+'\n','Function_'+input_function+'\n','Ownership_'+input_ownership+'\n', 'Sector_'+input_sector+'\n')'''
