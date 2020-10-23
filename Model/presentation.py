class Presentation:
    ID = "id"
    SPEAKER_ID = "speaker_id"
    SESSION_ID = "session_id"

    def get_schema():
        return {
               Presentation.SPEAKER_ID: "integer",
               Presentation.SESSION_ID: "integer"
        }