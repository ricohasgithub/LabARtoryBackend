import pyrebase
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Configuration key for realtime database with all permission (read + write) to true
config = {
    "apiKey": "AIzaSyBvnoDpe9mHxfbRUMga-31NxMJQTrYyyAo",
    "authDomain": "labartory.firebaseapp.com",
    "databaseURL": "https://labartory.firebaseio.com",
    "storageBucket": "labartory.appspot.com",
}

firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()

def stream_handler(message):

    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    procedure = "1. Measure the mass with electronic balance. 2. Mix the chemicals together."

    doc = nlp(procedure)

    nouns = [chunk.text for chunk in doc.noun_chunks]
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

    print(nouns)
    print(verbs)

# Get the datastream from the realtime database
data_stream = firebase_db.child("labs").stream(stream_handler)