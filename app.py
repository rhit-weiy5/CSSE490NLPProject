import pickle
import time
from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import h5py
import numpy as np
from tensorflow.keras.models import load_model

with open("tokenizer_model.pkl", "rb") as file:
    tokenizer = pickle.load(file)
SEQUENCE_LENGTH = 300
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"

model = load_model('model.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text_data = data['textData']
    #print("THIS IS TEH TYPE!!!!!  ")
    #print(type(text_data))
    sentiment = perform_sentiment_analysis(text_data)  
    return jsonify(sentiment=sentiment)

def perform_sentiment_analysis(text):

    print(text)
    sentiment = (predict(text))
    
    return sentiment

def decode_sentiment(score):
        return NEGATIVE if score < 0.5 else POSITIVE
    
def predict(text):
    start_at = time.time()
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score)

    return label

if __name__ == '__main__':
    app.run(debug=True)