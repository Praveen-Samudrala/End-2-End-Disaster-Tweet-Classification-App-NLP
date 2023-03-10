import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# --SETTING CONFIGS---
# Emojis - https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Disaster Tweet Classification", page_icon=":computer:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

# --ASSETS--
lottie_loan = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_mjuiybtp.json")
data_img = Image.open("images/data2.png")
labels = Image.open("images/labels.png")
keywords1 = Image.open("images/keywords1.png")
top_hashtags = Image.open("images/top_hashtags.png")
unique_wordcount = Image.open("images/unique_wordcount.png")
length = Image.open("images/length.png")
total_wordcount = Image.open("images/wordcount.png")
hashtag_count = Image.open("images/hashtag_count.png")



title = """<h1 style='text-align: center;'>Disaster Tweet Classification</h1>"""
body = ["""The Disaster Tweet Claasification Application classifies whether a tweet indicates an occured disaster or not.""",
        "This Application processess the text removing URLs, HTML Tags, Emojis and other Non-ASCII characters, punctuations and stopwords.",
        "Furthermore, the tweets are tokenized, Lemmatized and Encode them as part of Feature Enigneering.",
        "A custom desinged Classifier built with Stacking Naive Bayes, Logistic Regression and SVM Classifier is used for prediction.",
        "The app is launched using Streamlit and is Docker containerized."]

st.markdown(title, unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        for text in body:
            st.write(text)
    
    with col2:
        st_lottie(lottie_loan, key='lappy')
    


st.write('---')
text = "<h2 style='text-align: center;'>Data Analysis & Visualizations</h2>"
st.markdown(text, unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns((2,1))
    with col1:
        st.image(data_img, caption='Tweets Data')
    with col2:
        st.image(labels, caption='Target Classes')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(keywords1, caption='Most Frequent Keywords')
    with col2:
        st.image(top_hashtags, caption='Most Frequent Hashtags')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(unique_wordcount, caption='Unique Word Counts')
    with col2:
        st.image(total_wordcount, caption='Total Word Count per Tweet')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(hashtag_count, caption='Hastags per Tweet')
    with col2:
        st.image(length, caption='Word length')


with st.container():
    st.write("---")
    text = """<h4 style= 'text-align: center;'> Made by Praveen Samudrala </h4>"""
    st.markdown(text, unsafe_allow_html=True)

# Session State
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'