import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pickle
import streamlit as st

data = pd.read_csv('myBca.csv')
data['sentimen'] = data['sentimen'].map({'positif': 1, 'negatif': 0})
X = data['clean_text']
y = data['sentimen']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)

vectorizer = TfidfVectorizer(use_idf=True, strip_accents='ascii')
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

svm_model = SVC(kernel='linear', random_state=44)
svm_model.fit(X_train_vect, y_train)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

with open('svm_model.pkl', 'wb') as model_file:
    pickle.dump(svm_model, model_file)

def load_model(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)

def predict_sentiment(model, text, vectorizer):
    text_vect = vectorizer.transform([text])
    prediction = model.predict(text_vect)[0]
    sentiment_map = {0: 'negatif', 1: 'positif'}
    return sentiment_map[prediction]

def main():
    st.title('SVM Sentiment Prediction App')

    html_temp = """
    <div style="background-color:yellow;padding:10px">
    <h2 style="color:black;text-align:center;">Sentiment Classification Using SVM</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    review_text = st.text_area('Enter the text for sentiment analysis', 'Type here...')

    if st.button('Predict Sentiment'):
        if review_text:
            vectorizer = load_model('vectorizer.pkl')
            model = load_model('svm_model.pkl')
            result = predict_sentiment(model, review_text, vectorizer)
            st.success(f'The predicted sentiment is: {result}')
        else:
            st.warning('Please enter text for sentiment analysis.')

if __name__ == '__main__':
    main()
