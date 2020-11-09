from bs4 import BeautifulSoup
import requests

from film_details_searcher.models.film_details import FilmDetails

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}


class FilmwebScraper:
    def __init__(self, link_to_film):
        self._link_to_film = link_to_film

    @property
    def link_to_film(self):
        return self._link_to_film

    def fetch_film_details(self):
        request = requests.get(self._link_to_film, headers=headers)
        film_details = self._fetch_film_details_from_request(request)
        return film_details

    def _fetch_film_details_from_request(self, request):
        soup = BeautifulSoup(request.text, "html.parser")
        film_title = soup.findChild("h1", {"class": "filmCoverSection__title"}).text
        film_descripton = soup.find("div", {"class": "filmPosterSection__plot"}).text
        premiere_year = soup.find("span", {"class": "filmCoverSection__year"}).text
        film_time = soup.find("span", {"class": "filmCoverSection__filmTime"}).text
        film_rating_value = soup.find("span", {"class", "filmRating__rateValue"}).text
        film_rating_count = soup.find("span", {"class": "filmRating__count"}).text
        film_details = FilmDetails(film_title, film_descripton, premiere_year, film_time, film_rating_value, film_rating_count)
        return film_details
