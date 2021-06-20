from flask import Blueprint, request, jsonify
from .models import Event
from .serializers import event_schema

scan_api = Blueprint('api', __name__)


@scan_api.route('/')
def home():
    return "Hello World"

@scan_api.route('/scan', methods=['POST'])
def get_calendar_info():
    text = request.json['text']

    title = ""
    description = ""
    start_date = ""
    end_date = ""
    start_time = ""
    end_time = ""

    new_event = Event(title, description, start_date, end_date, start_time, end_time)
    new_event_data = event_schema.jsonfiy(new_event)

    return new_event_data


# Summary, Description, Start (Time), End 

# {
#   "summary: "", 
#   "description": "", 
#   "start": {
#       "time": ""
#   }, 
#    "end": {
#       "time": ""
#   }
# }