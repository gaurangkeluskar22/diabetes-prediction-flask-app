from flask import Flask
import pickle

app = Flask(__name__)
model = pickle.load(open("diabetes_detection/finalized_model.sav", 'rb'))

from diabetes_detection import routes
