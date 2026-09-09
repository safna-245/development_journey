#title,language,duration,year,rating

movies = [
    ["kgf","kannada",150,2005,8],
    ["balan","malayalam",130,2026,7],
    ["ramayanam","hindi",150,2026,8.5],
    ["abcd","malayalam",160,2008,6],
    ["goatlife","malayalam",150,2024,9],

]
#display duration,year,rating
print(movies[3][2:])

#display all movie_title

all_movies = [m[0] for m in movies]

print(all_movies)

#display all movie years

all_years = [m[3] for m in movies]

print(all_years)
#display all movie languages

all_languages = [m[1] for m in movies]

print(all_languages)