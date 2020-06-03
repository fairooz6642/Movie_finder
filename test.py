# Cant use imdbpy as lxml isnt working
# So instead we use web-scraping through beautiful soup
# It seems the problem was in choosing the default interpreter which was the base directory of Python.
# So we changed it to Conda interpreter.
# So, problem solved.

import imdb

moviesDB = imdb.IMDb()

# Finding out the required traits of the movies.
# Please enter the names of the seven movies you liked.
# Make sure the spellings are correct.
# First movie:
Year = 2000
IM=10.0
List1 = ['Comedy', 'Drama']
List2 = ['Road', 'Comedy-drama', 'Romance']
def mamamia (name):
    movies = moviesDB.search_movie(name)
    id = movies[0].getID()
    movie=moviesDB.get_movie(id)
    year=movie['year']
    rating=movie['rating']
    Gen = movie['genres']
    global Year
    if year<Year:
        Year=year
    global IM
    if rating<IM:
        IM=rating

    

# First movie:
mamamia ('Rushmore')
# Second movie:
mamamia ('Broken Flowers')
# Third movie:
mamamia ('Darjeeling Limited')
# Fourth movie:
mamamia ('Forest Gump')
# Fifth movie:
mamamia ('La La Land')
# Sixth movie:
mamamia ('Groundhog Day')
# Seventh movie:
mamamia ('Whiplash')


top=moviesDB.get_top250_movies()
for x in range(250):
    id=top[x].getID()
    movie=moviesDB.get_movie(id)
    Gen=movie['genres']
    if 'Biography' in Gen and movie['year']>=Year:
        print(top[x])
        
