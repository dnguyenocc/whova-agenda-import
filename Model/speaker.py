class Speaker:
    ID = "id"
    NAME = "name"

    def get_schema():
        return {
            "id": "integer PRIMARY KEY AUTOINCREMENT",
            "name": "text"
        }