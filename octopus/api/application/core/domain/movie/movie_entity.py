from datetime import datetime


class MovieEntity:
    def __init__(self, title: str, release_date: datetime):
        self.title = title
        self.release_date = release_date

    def __eq__(self, other):
        if isinstance(other, MovieEntity):
            return self.title == other.title and self.release_date == other.release_date
        return False
