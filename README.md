<h1 align="center">Disaster Tweet Classification App</h1>

# Overview: 

The Disaster Tweet Claasification Application classifies whether a tweet indicates an occured disaster or not.  
This Application processess the text removing URLs, HTML Tags, Emojis and other Non-ASCII characters, punctuations and stopwords. Furthermore, the tweets are tokenized, Lemmatized and Encode them as part of Feature Enigneering.  
A custom desinged Classifier built with Stacking Naive Bayes, Logistic Regression and SVM Classifier is used for prediction.

# Project Planning:

## 1.  Data Exploration
  * Distribution of target variable.
  * Visualization of various characteristics in Disaster and Non-disaster Tweets.
  * Looking at Tweets analyzing the necessary cleaning strategies.  

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/data1.png"
  alt="Data_Sample"
  title="Data Sample"/>  

## 2. Data Preprocessing  
  * Lower casing.
  * Clean with RegExp.
    - URLs
    - HTML Tags
    - Non-Ascii characters.
    - Emojis.
  * Remove Punctuations.
  * Remove Stopwords.
  * Lemmatization.
  * Feature Encoding - Experimented with BagofWords and TF-IDF Vectorization.

## 3. Model Building and Evaluation
  * Model Experimentation 1
    - Support Vector Machines
    - Multinomial Naive Bayes
    - Decision Trees
    - Random Forest Classifier
    - LightGBM
    - CatBoost
    - XGBoost

  * Model Experimentation 2
    - Scaling + Logistic Regression

  * Model Experimentation 3
    - Naive Bayes  \  
    - Logistic Reg - Logistic -> Output  
    - SVM Classif  /

  * Evaluation

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/performance.png"
  alt="performance"
  title="performance"/>

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/performance1.png"
  alt="performance2"
  title="performance2"/>

## 4. Inference function
  * Training a model on whole dataset (X and y) without splitting.
  * Function "assess_customer" to assess new customers whether they payback loan or not.
  * Check model predictions on new customer.

## 5. Prediction App with Streamlit
<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/homepage1.png"
  alt="Home Page_1"
  title="Home Page"/>

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/homepage2.png"
  alt="Home Page_2"
  title="Home Page"/>

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/homepage3.png"
  alt="Home Page_3"
  title="Home Page"/>

<img
  src="https://github.com/Praveen-Samudrala/End-2-End-Disaster-Tweet-Classification-App-NLP/blob/main/images/result.png"
  alt="Predictor_1"
  title="Predictor"/>

  
## Launch
Install the dependencies via: 
```
pip install -r requirements.txt
```
And have Docker installed with Docker Daemon running.

Run the application using:

```
docker-compose up
```
This app was launched on AWS Elastic Beanstalk.
