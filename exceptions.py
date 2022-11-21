class NewsInfoException(Exception):
    ...


class NewsInfoNotFoundError(NewsInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Nie znaleziono wpisu"


class NewsInfoInfoAlreadyExistError(NewsInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Taki news juz istnieje"