from flask import Blueprint, request, jsonify
from .models import Event
from .serializers import event_schema

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet 
from nltk.stem import PorterStemmer, WordNetLemmatizer
import numpy as np


scan_api = Blueprint('api', __name__)


# Helper Functions

def get_part_of_speech():
    return ""


# Routes

@scan_api.route('/')
def home():
    return "Hello World"

@scan_api.route('/scan', methods=['POST'])
def get_calendar_info():
    text = request.json['text']

    title = ""
    description = ""
    location = ""
    start_date = ""
    end_date = ""
    start_time = ""
    end_time = ""

    new_event = Event(title, description, location, start_date, end_date, start_time, end_time)
    new_event_data = event_schema.jsonfiy(new_event)

    return new_event_data
