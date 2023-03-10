import numpy as np
import pickle
import pandas as pd
import re
import string
import spacy
nlp = spacy.load("en_core_web_sm")
import streamlit as st 


tfidf, mnb, logreg, stack = pickle.load(open('objects.pkl', 'rb'))

# Preprocess using Spacy
def preprocess(data):
  '''The below preprocessing is performed.
    1. Lower casing
    2. Cleaning with RegExp
    3. Tokenizing
    4. Remove Punctuations
    5. Remove Stopwords
    6. Lemmatize
  '''
  # Converting all the text data to its lower form
  data = data.lower()

  # Cleaning with RegExp
  # Removing URLs from the text data
  data = re.sub(r'https?://\S+|www\.\S+', '', data)
  # Removing HTML Tags
  data = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", '', data)
  #Removing Non-Ascii
  data = re.sub(r'[^\x00-\x7f]','', data)
  # Removing Emojis
  emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
  data = emoji_pattern.sub(r'', data)

  doc = nlp(data)
  # Remove Punctuations
  data = [token for token in doc if token.text not in string.punctuation]
  # Remove stopwords
  data = [token for token in data if not token.is_stop]
  # Lemmatize
  data = ' '.join([token.lemma_ for token in data])

  return data

def predict(text):
    text_cleaned = preprocess(text)
    # TFIDF vectorizer
    input_tokens = tfidf.transform([text_cleaned])

    # MultiNB, Stacking, LogReg models predictions
    stack_predict = stack.predict(input_tokens)
    if stack_predict == 1: return """<h3 style="color:white;text-align:center;"> Indicates a Disaster </h3>"""
    else: return """<h3 style="color:white;text-align:center;">Does not indicates a Disaster </h3>"""


def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Disaster Tweet Classification App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    input_text = st.text_input('Enter new Tweet',"Type Here")
    
    with st.container():
        with st.columns(5)[2]:
            flag = st.button('Submit')

    with st.container():
        if flag:
            result = predict(input_text)
            st.markdown(result, unsafe_allow_html=True)

    # if st.button("Predict"):
    #     pred = predict(input_text)
    #     if pred == 1:
    #         result = "It's a Disaster"
    #     else:
    #         result = "It's NOT a Disaster"
    # st.success(result)
    if st.button("About"):
        st.text("Built by Praveen Samudrala using Streamlit")

if __name__=='__main__':
    main()