import pandas as pd
import pickle

def getSentiment(text):
    a = [text]
    count_vectorizer = pickle.load(open('./models/countVectorizer.sav','rb'))
    tfidf_vectorizer = pickle.load(open('./models/tfidfVectorizer.sav','rb'))
    model = pickle.load(open('./models/GBModel.sav','rb'))
    temp = tfidf_vectorizer.transform(count_vectorizer.transform(a))
    return(model.predict(temp))