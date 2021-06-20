from . import db 

# Create models here 

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    location = db.Column(db.String(250))
    start_date = db.Column(db.String(250))
    end_date = db.Column(db.String(250))
    start_time = db.Column(db.String(250))
    end_time = db.Column(db.String(250))

    def __init__(self, title, description, location, start_date, end_date, start_time, end_time):
        self.title = title
        self.description = description
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time