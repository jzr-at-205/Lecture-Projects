import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import spacy

# Load the pre-trained model
nltk.download('punkt')
nltk.download('stopwords')

# function to process the text
def process_text(text):

    # tokenize the text
    tokens = word_tokenize(text)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # then remove punctiation
    tokens = [token for token in tokens if token.isalpha()]

    return ' '.join(tokens)

# implement intent detection
# load pretrained model

nlp = spacy.load('en_core_web_sm')

def detect_intent(text):
    
    # then prepocess the text
    text = process_text(text)

    # use text using nlp model
    doc = nlp(text)

    # detect the intent
    intent = None
    for ent in doc.ents:
        if ent.label_ == 'INTENT':
            intent = ent.text
            break

    return intent

# following, implement entity recognition
# and load pretrained model

nlp = spacy.load('en_core_web_sm')

def recognize_entities(text):

    # preprocess the text
    text = process_text(text)

    # process text using nlp model
    doc = nlp(text)
    
    # recognize entities
    entities = []

    for ent in doc.ents:
        entities.append((ent.text, ent.label))

    return entities

# after, implement text classification

def classify_text(text):

    # preprocess the text
    text = process_text(text)

    # vector-size text
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform([text]) 

    # train model
    clf = MultinomialNB()
    clf.fit(x, ['category'])   

    # classify text
    prediction = clf.predict(x)

    return prediction[0]
