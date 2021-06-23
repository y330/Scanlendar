from flask import Blueprint, request, jsonify, send_from_directory
from .models import Event
from .serializers import event_schema

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
import numpy as np


scan_api = Blueprint('api', __name__)


# Helper Functions

def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synset(word)
    pos_counts = Counter()
    pos_counts["n"] = len(
        [item for item in probable_part_of_speech if item.pos() == "n"])
    pos_counts["v"] = len(
        [item for item in probable_part_of_speech if item.pos() == "v"])
    pos_counts["a"] = len(
        [item for item in probable_part_of_speech if item.pos() == "a"])
    pos_counts["r"] = len(
        [item for item in probable_part_of_speech if item.pos() == "r"])

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]

    return most_likely_part_of_speech


def determine_details(text):
    event_details = {
        "title": "",
        "description": "",
        "location": "",
        "start_date": "",
        "end_date": "",
        "start_time": "",
        "end_time": "",
    }

    tokenized_text = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    return event_details

# Routes



@scan_api.route("/")
def base():
    return send_from_directory('svelte/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)


@scan_api.route("/<path:path>")
def home(path):
    return send_from_directory('svelte/public', path)


@scan_api.route("/rand")
def hello():
    return str(random.randint(0, 100))


@scan_api.route('/home', methods=['POST'])
def get_calendar_info():
    text = request.json['text']

    event_details = determine_details(text)

    title = event_details["title"]
    description = event_details["description"]
    location = event_details["location"]
    start_date = event_details["start_date"]
    end_date = event_details["end_date"]
    start_time = event_details["start_time"]
    end_time = event_details["end_time"]

    new_event = Event(title, description, location,
                      start_date, end_date, start_time, end_time)
    new_event_data = event_schema.jsonfiy(new_event)

    return new_event_data
