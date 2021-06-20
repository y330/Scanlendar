from . import ma 

# Create serializers here

class EventSchema(ma.Schema):
    class Meta:
        fields = ('title', 'description', 'location', 'start_date', 'end_date', 'start_time', 'end_time')

event_schema = EventSchema(strict=True)