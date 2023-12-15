class movie:
    def __init__(self):
        movie_name=""
        movie_genre=""
        price=0
        rating=0
        actor=""
        year_of_release=0
    def newmovies(self):
        self.movie_name=input("enter the movie name:")
        self.movie_genre=input("enter the movie genre:")
        self.price=int(input("enter the price of the movie:"))
        self.rating=input("enter the rating of movies:")
        self.actor=input("enter the actor of the movie:")
        self.year_of_release=int(input("enter the year of release:"))

    def view(self):
        print(f"movie name:{self.movie_name} movie genre:{self.movie_genre} price:{self.price} rating:{self.rating} actor:{self.actor} year of release:{self.year_of_release}")
class moviefind(movie):
    movie_genre=""
    rating=0
    year_of_release=0
    def findmovies(self):
        self.movie_genre=input("enter the movie genre:")
        self.rating=int(input("enter the rating of the movie:"))
        self.year_of_release=int(input("enter the year of release:"))
class mymovies(moviefind) :
    def matching_movie_search(self):
              if (
            self.movie_genre_search == self.movie_genre
            and self.rating_search == self.rating
            and self.year_of_release_search == self.year_of_release
        ):
               self.view()
            
if __name__=="__main__":
            
                        movie=mymovies()
                        movie.newmovies()
                        movie.findmovies()
                        movie.matching_movie_search()


         

