class Movie:
    def __init__(self, title, id, rating) -> None:
        self._title = title
        self._id = id
        self._rating = rating
        self.url = "https://www.imdb.com/title/"+self._id
        