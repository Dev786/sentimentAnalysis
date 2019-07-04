import pandas as pd
import pickle


count_vectorizer = pickle.load(open('./models/countVectorizer.sav','rb'))
tfidf_vectorizer = pickle.load(open('./models/tfidfVectorizer.sav','rb'))
model = pickle.load(open('./models/GBModel.sav','rb'))

a = ['I am bad','He is the best PM']

temp = tfidf_vectorizer.transform(count_vectorizer.transform(a))
print(model.predict(temp))