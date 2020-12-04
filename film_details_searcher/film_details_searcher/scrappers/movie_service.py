from abc import ABC, abstractmethod


class MovieService(ABC):

    def get_movie(self, link_to_movie: str):
        if not isinstance(link_to_movie, str):
            raise TypeError('Link only accepted as str')
        return self._fetch_movie_from_link(link_to_movie)

    @abstractmethod
    def _fetch_movie_from_link(self, link_to_movie):
        pass
