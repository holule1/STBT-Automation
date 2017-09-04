
class Channel(object):

    def __init__(self):
        self.__prosieben = ("The Voice",
                            "Circus Halligalli",
                            "Greys Anatomy",
                            "Containment")

        self.__sateins = ("The Taste",
                          "Criminal Minds")

    # Detect which movie on which Channel available is.
    def detect(self, moviename):
        if self.__prosieben.__contains__(moviename):
            return "prosieben"
        elif self.__prosieben.__contains__(moviename):
            return "sateins"
        else:
            return None

    # Which movies are Available to test.
    def movies_available(self):
        movies = "Available Media:\n\nProsieben: \t"
        for p in self.__prosieben:
            movies += p + " : "
        movies += "\nSateins: \t"
        for i in self.__sateins:
            movies += i + " : "
        return movies
