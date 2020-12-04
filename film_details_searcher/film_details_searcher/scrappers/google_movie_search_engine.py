from film_details_searcher.models.search_result import SearchResult
from film_details_searcher.scrappers.movie_search_engine import MovieSearchEngine
from bs4 import BeautifulSoup
import requests
import urllib.parse
from film_details_searcher.scrappers.custom_headers import CUSTOM_HEADERS


class GoogleMovieSearchEngine(MovieSearchEngine):

    def _do_search(self, movie_title):
        fetched_data = self._fetch_all_data_from_search_engine(movie_title)
        filtered_results = list(filter(self._filter_movie_service_result, fetched_data))
        return filtered_results

    def _fetch_all_data_from_search_engine(self, movie_title):
        all_pages_filtered = False
        page_counter = 0
        fetched_data = []
        while not all_pages_filtered:
            try:
                if page_counter == 0:
                    search_link = self._prepare_search_link_for_first_page(movie_title)
                else:
                    search_link = self._fetch_next_page_link(request)
                request = self._make_request_with_search_link(search_link)
                single_fetch_results = self._fetch_data_from_request(request)
                fetched_data.extend(single_fetch_results)
                page_counter += 1
            except (AttributeError, IndexError):
                all_pages_filtered = True
        return fetched_data

    @staticmethod
    def _prepare_search_link_for_first_page(search_term):
        base = "search?q="
        encoded_search_term = urllib.parse.quote(f"{search_term} filmweb")
        return ''.join([base, encoded_search_term])

    @staticmethod
    def _make_request_with_search_link(search_link):
        request = requests.get(f"https://www.google.com/{search_link}", headers=CUSTOM_HEADERS)
        return request

    @staticmethod
    def _fetch_data_from_request(request):
        soup = BeautifulSoup(request.text, "html.parser")
        links = soup.findAll("div", {"class": "yuRUbf"})
        fetched_data = []
        for link in links:
            item_text = link.find("h3").text
            item_link = link.find("a").attrs["href"]
            sr = SearchResult.parse(item_text, item_link)
            fetched_data.append(sr)
        return fetched_data

    def _fetch_next_page_link(self, request):
        soup = BeautifulSoup(request.text, "html.parser")
        footer = soup.find("div", {"id": "foot"})
        next_page_button = footer.find_all("td", {"class": "d6cvqb"})[-1]
        next_page_link = next_page_button.find("a").attrs["href"]
        return next_page_link