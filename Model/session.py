class SessionType:
    SESSION = "Session"
    SUBSESSION = "Sub"


class Session:
    ID = "id"
    DATE = "date"
    START_TIME = "start_time"
    END_TIME = "end_time"
    TITLE = "title"
    LOCATION = "location"
    DESCRIPTION = "description"

    def __init__(self,date,start_time,end_time,title,location="",description=""):
        self.data = {
            Session.DATE: date,
            Session.START_TIME: start_time,
            Session.END_TIME: end_time,
            Session.TITLE: title,
            Session.LOCATION: location,
            Session.DESCRIPTION: description
        }

    def add_speaker(self, speaker_name):
        self.speakers.add(speaker_name)

    def set_session_type(self, session_type):
        self.session_type = session_type


    def get_schema():
        return {
            "id": "integer PRIMARY KEY",
            "date": "date",
            "start_time": "datetime",
            "end_time": "datetime",
            "title": "text",
            "location": "text",
            "description": "text"
        }
