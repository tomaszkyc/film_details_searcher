from bs4 import BeautifulSoup
import requests
import urllib.parse

from film_details_searcher.models.search_result import SearchResult
from film_details_searcher.models.select_menu import SelectMenu
from film_details_searcher.scrappers.filmweb_scraper import FilmwebScraper

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}


def _get_search_term():
    search_term = input("Type film title you want to see details: ")
    return search_term


def _prepare_search_link_for_first_page(search_term):
    base = "search?q="
    encoded_search_term = urllib.parse.quote(f"{search_term} filmweb")
    return ''.join([base, encoded_search_term])


def _make_request_with_search_link(search_link):
    request = requests.get(f"https://www.google.com/{search_link}", headers=headers)
    return request


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


def _fetch_next_page_link(request):
    soup = BeautifulSoup(request.text, "html.parser")
    footer = soup.find("div", {"id": "foot"})
    next_page_button = footer.find_all("td", {"class": "d6cvqb"})[-1]
    next_page_link = next_page_button.find("a").attrs["href"]
    return next_page_link


def _fetch_all_data_from_search_engine(search_term):
    all_pages_filtered = False
    page_counter = 0
    fetched_data = []
    while not all_pages_filtered:
        try:
            if page_counter == 0:
                search_link = _prepare_search_link_for_first_page(search_term)
            else:
                search_link = _fetch_next_page_link(request)
            request = _make_request_with_search_link(search_link)
            single_fetch_results = _fetch_data_from_request(request)
            fetched_data.extend(single_fetch_results)
            page_counter += 1
        except (AttributeError, IndexError):
            print("All pages viewed to find the film")
            all_pages_filtered = True
    return fetched_data


def _filter_filmweb_movies(search_result):
    link = str(search_result.link)
    return "https://www.filmweb.pl/film/" in link


def _show_select_menu(menu_items):
    select_menu = SelectMenu(menu_items)
    selected_item = select_menu.show_menu_and_wait_for_result()
    filmweb_scraper = FilmwebScraper(selected_item.link)
    film_details = filmweb_scraper.fetch_film_details()
    print(film_details)


def _main():
    search_term = _get_search_term()
    fetched_data = _fetch_all_data_from_search_engine(search_term)
    filtered_results = list(filter(_filter_filmweb_movies, fetched_data))
    if len(filtered_results) > 0:
        _show_select_menu(filtered_results)
    else:
        print("No results for given film title")


class FilmSearcher:
    def __init__(self):
        pass

    def start_searching(self):
        _main()
