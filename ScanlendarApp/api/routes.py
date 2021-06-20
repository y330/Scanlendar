from flask import Blueprint

scan_api = Blueprint('api', __name__)


@scan_api.route('/')
def home():
    return "Hello World"