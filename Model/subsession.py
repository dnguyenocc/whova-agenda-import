class Subsession:
    PARENT_SESSION_ID = "parent_session_id"
    CHILD_SESSION_ID = "child_session_id"

    def get_schema():
        return {
            Subsession.PARENT_SESSION_ID: "integer",
            Subsession.CHILD_SESSION_ID: "integer"
        }