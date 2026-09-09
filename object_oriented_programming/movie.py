"""
Movie title,language,year,director,genre 
    -setmovie(title,language,year,director,genre)
    -getmovie(self)
"""
class Movie:

    title:str

    language:str

    year:int

    director:str

    genre:str

    def __init__(self,title,language,year,director,genre):

        self.title =title

        self.language = language

        self.year = year

        self.director = director

        self.genre = genre

    def get_movie(self):

        print(self.title,self.language,self.year,self.director,self.genre)

br_instance = Movie("Bramayugam","Malayalam",2024,"Rahul sadasivan","Thriller")

rrr_instance = Movie("RRR","Telugu",2022,"Rajamouli","action")

br_instance.get_movie()

rrr_instance.get_movie()


