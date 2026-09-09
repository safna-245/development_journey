class Movie:

    def __init__(self):

        self.movies = [
            {"id":1,"title":"Banglore Days","year":2014,"genre":"Drama","rating":8.3,"runtime":"170 minutes","director":"Anjali Menon"}
        ]

    def post(self,**kwargs):

        self.movies.append(kwargs)

        print("record has been created...")

    def get(self):

        if len(self.movies)==0:

            print("no records found..")

        else:

            for m in self.movies:

                print(m)

    def retrieve(self,id=None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        print(movie)

    def put(self,id=None,**kwargs):

        movie = [m for m in self.movies if m.get("id")==id][0]

        movie.update(kwargs)

        print(movie)

    def delete(self,id=None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        self.movies.remove(movie)

        print("deleted..")

        self.get()


movie_instance = Movie()

movie_instance.post(id=2,title="Dangal",year=2016,genre="sports",rating=8.3,runtime="160 minutes",director="Nitesh Tiwari")

movie_instance.get()

movie_instance.retrieve(id=2)

movie_instance.put(id=2,runtime="16o min",year="2017")

movie_instance.delete(id=2)

