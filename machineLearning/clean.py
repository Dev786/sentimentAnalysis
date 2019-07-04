from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize

def cleanText(sentence):
    sentence = sentence.lower()
    stopwords_clean = stopwords.words('english')
    tokens = [token for token in word_tokenize(sentence) if token not in stopwords_clean]
    finalResult = []
    for token in tokens:
        token_clean = ""
        for c in token:
            if c not in getPuctAndDigits():
                token_clean += c
        finalResult.append(token_clean)
    return " ".join(finalResult).strip()

def cleanSentence(sentence_list):
    data = sentence_list.split("\n")
    data_to_return = []
    for sent in data:
        tokens = ""
        for token in word_tokenize(sent):
            tokens += (cleanText(token))+ " "
        data_to_return.append(tokens.strip())
    return data_to_return

def getPuctAndDigits():
    punc_list = [punct for punct in string.punctuation]
    digits = [digit for digit in string.digits]
    punc_digits = []
    for p in punc_list:
        punc_digits.append(p)
    
    for p in digits:
        punc_digits.append(p)

    return punc_digits

print(cleanText("Hello World This is Ryan ......."))