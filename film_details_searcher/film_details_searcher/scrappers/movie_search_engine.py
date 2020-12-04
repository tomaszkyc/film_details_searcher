from abc import ABC, abstractmethod

from film_details_searcher.models.search_result import SearchResult


class MovieSearchEngine(ABC):

    def search(self, movie_title: str):
        if not isinstance(movie_title, str):
            raise TypeError("Movie title can be only str type")
        return self._do_search(movie_title)

    @abstractmethod
    def _do_search(self, movie_title):
        pass

    @staticmethod
    def _filter_movie_service_result(search_result: SearchResult):
        link = str(search_result.link())
        return link.startswith(r"https://www.filmweb.pl/film/")
