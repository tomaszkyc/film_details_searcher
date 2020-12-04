import pytest

from film_details_searcher.models.movie import Movie
from film_details_searcher.scrappers.filmweb_movie_service import FilmwebMovieService
from film_details_searcher.scrappers.movie_service import MovieService


@pytest.fixture
def movie_service():
    return FilmwebMovieService()


@pytest.fixture
def valid_movie_link():
    return r'https://www.filmweb.pl/film/Green+Book-2018-809630'


def test_should_find_film_by_correct_link(valid_movie_link, movie_service: MovieService):
    movie: Movie = movie_service.get_movie(valid_movie_link)
    assert movie is not None
    assert len(movie.details) > 0


def test_should_raise_exception_if_movie_link_has_incorrect_type(movie_service: MovieService):
    with pytest.raises(TypeError) as e:
        movie_service.get_movie(None)