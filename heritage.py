class Film:

    def __init__(self,titre):
        self.titre = titre
    def watch(self):
        print("Bon visionnage")


class FilmCassette(Film):

    def __init__(self,titre):
        super().__init__(titre)
        self.magnetic_type = True

    def rewind(self):
        print("c'est long à rombiner")
        self.magnetic_type = True


film = Film("2001: l'odyssée de l'espace")
film_cassette = FilmCassette("The 100")

print(film_cassette.titre)
