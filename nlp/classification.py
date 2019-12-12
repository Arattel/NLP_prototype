import pickle
import re
from stop_words import get_stop_words
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.naive_bayes import GaussianNB, ComplementNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

from nltk.stem import WordNetLemmatizer

lm = WordNetLemmatizer()

def lemmatize(word):
    return lm.lemmatize(word)


def scrub_words(text):
    text = re.sub("(<.*?>)", "", text)

    text = re.sub("(\\W|\\d)", " ", text)

    text = text.strip()
    return text


def preprocess_text(content):
    content = content.lower()
    content = content.split()
    content = list(map(scrub_words, content))
    content = list(filter(lambda x: x not in stopWords and len(x), content))
    content = list(map(lemmatize, content))
    return " ".join(content)


loaded_model = pickle.load(open('nlp/pretrained_nb', 'rb'))
le = pickle.load(open('nlp/label_encoder', 'rb'))
tf = pickle.load(open("nlp/vectorizer", 'rb'))


def classify(text):
    return le.inverse_transform(loaded_model.predict(tf.transform([preprocess_text(text)])))
