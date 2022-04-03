from turtle import title
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
print(soup.find("ImageMeta"))
# all_movies = soup.find_all(name="h3", class_="title")
# movies_titles = [movie.getText() for movie in all_movies]
# movies = movies_titles[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
