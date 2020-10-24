from enum import Enum
class SessionType(Enum):
    Session = 1
    Sub = 2


class Session:
    ID = "id"
    DATE = "date"
    START_TIME = "start_time"
    END_TIME = "end_time"
    TYPE = "type"
    TITLE = "title"
    LOCATION = "location"
    DESCRIPTION = "description"
    SPEAKER = "speaker"

    def get_schema():
        return {
            "id": "integer PRIMARY KEY AUTOINCREMENT",
            "date": "date",
            "start_time": "datetime",
            "end_time": "datetime",
            "type": "integer",
            "title": "text",
            "location": "text",
            "description": "text"
        }
