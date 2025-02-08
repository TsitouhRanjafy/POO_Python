class Film:

    def __init__(self,titre):
        self.titre = titre

class FilmCassette(Film):
    def __init__(self,titre):
        self.titre = titre
        self.magnetic = True

film_cassette = FilmCassette("The 100")

print(film_cassette.titre)