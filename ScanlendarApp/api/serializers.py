from . import ma 


class EventSchema(ma.Schema):
    class Meta:
        fields = ('title', 'description', 'start_date', 'end_date', 'start_time', 'end_time')

event_schema = EventSchema(strict=True)