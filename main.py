import imdb
hr=imdb.IMDb()
movie_name=input("enter the movie name : ")
movies=hr.search_movie(str(movie_name))
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['title']
rating=movie['rating']
genre=movie['genre']
year=movie['year']
cast=movie['cast']
list_of_cast=','.join(map(str,cast))
print("title :",title) 
print("rating :",rating)
print("genre :",genre)
print("year of release : ",year)
print("full cast : ",list_of_cast )



