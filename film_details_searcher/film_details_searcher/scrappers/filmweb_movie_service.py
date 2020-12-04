from film_details_searcher.models.movie import Movie
from film_details_searcher.scrappers.custom_headers import CUSTOM_HEADERS
from film_details_searcher.scrappers.movie_service import MovieService
from bs4 import BeautifulSoup
import requests


class FilmwebMovieService(MovieService):

    def _fetch_movie_from_link(self, link_to_movie):
        request = requests.get(link_to_movie, headers=CUSTOM_HEADERS)
        film_details = FilmwebMovieService._parse_request_to_movie(request)
        return film_details

    @staticmethod
    def _parse_request_to_movie(request):
        soup = BeautifulSoup(request.text, "html.parser")
        title = soup.findChild("h1", {"class": "filmCoverSection__title"}).text
        description_pl = soup.find("div", {"class": "filmPosterSection__plot"}).text
        premiere_year = soup.find("span", {"class": "filmCoverSection__year"}).text
        movie_time = soup.find("span", {"class": "filmCoverSection__filmTime"}).text
        movie_rating_value = soup.find("span", {"class", "filmRating__rateValue"}).text
        movie_rating_count = soup.find("span", {"class": "filmRating__count"}).text
        movie_details = {"title": title, "description_pl": description_pl, "premiere_year": premiere_year,
                         "movie_time": movie_time, "movie_rating_value": movie_rating_value,
                         "movie_rating_count": movie_rating_count}
        movie = Movie.parse(movie_details)
        return movie
