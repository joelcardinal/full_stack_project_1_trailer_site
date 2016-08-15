# Python 2.7

import fresh_tomatoes
import webbrowser
import media


big_lebowski = media.Movie(
    'tt0118715',
    'https://www.youtube.com/watch?v=cd-go0oBF4Y')

reservoir_dogs = media.Movie(
    'tt0105236',
    'https://www.youtube.com/watch?v=vayksn4Y93A')

citizen_kane = media.Movie(
    'tt0033467',
    'https://www.youtube.com/watch?v=8dxh3lwdOFw')

superbad = media.Movie(
    'tt0829482',
    'https://www.youtube.com/watch?v=MNpoTxeydiY')

abyss = media.Movie(
    'tt0096754',
    'https://www.youtube.com/watch?v=4zbpL3LeW7k')

blade_runner = media.Movie(
    'tt0083658',
    'https://www.youtube.com/watch?v=KPcZHjKJBnE')

movies = [
    big_lebowski,
    reservoir_dogs,
    citizen_kane,
    superbad,
    abyss,
    blade_runner]

fresh_tomatoes.open_movies_page(movies, "Joel's Favorite Movies!")
