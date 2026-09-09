"""
Song  id,moviename,title,trackno,singer,duration
        -setsong(id,moviename,title,trackno,singer,duration)
        -getsong()

"""

class Song:

    id: int
    moviename:str
    title:str
    trackno:int
    singer:str
    duration:float

    def __init__(self,id,moviename,title,trackno,singer,duration):

        self.id = id
        self.moviename = moviename
        self.title = title
        self.trackno = trackno
        self.singer = singer
        self.duration = duration

    def get_song(self):

        print(self.id,self.moviename,self.title,self.trackno,self.singer,self.duration)

s_instance = Song(1,"saiyaraa","saiyaraa",1,"Faheem Abdullah",6.10)

d_instance = Song(2,"RRR","Dosti",1,"Amit Trivedi",5.40)

s_instance.get_song()

d_instance.get_song()


