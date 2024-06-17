from bs4 import BeautifulSoup
import lxml
import requests
from pprint import pprint
import notification_manager


website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=website)
soup = BeautifulSoup(response.text, "lxml")
pprint(soup)

movies = soup.find_all(name="h3", class_="title")

movies_out = []
for movie in movies:
    new_movie = movie.text.split(") ")
    try:
        movies_out.append({"rank": new_movie[0], "title": new_movie[1]})
    except IndexError:
        print(f"{new_movie} caused an error")
        new_movie = new_movie[0].split(": ")
        movies_out.append({"rank": new_movie[0], "title": new_movie[1]})
movies_out.sort(key=lambda m: int(m["rank"]))

with open("movies.txt", "w") as file:
    file.writelines(f"{movie["rank"]}: {movie["title"]}\n" for movie in movies_out)
