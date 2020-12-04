import pytest

from film_details_searcher.models.search_result import SearchResult
from film_details_searcher.scrappers.movie_search_engine import MovieSearchEngine


@pytest.fixture
def sample_search_result():
    return SearchResult.parse('Titanic', 'https://www.filmweb.pl/film/titanic...')


def test_if_cannot_create_instance_of_class():
    with pytest.raises(TypeError) as exception:
        MovieSearchEngine()


def test_if_filter_movie_service_result_passing(sample_search_result: SearchResult):
    assert MovieSearchEngine._filter_movie_service_result(sample_search_result)


def test_should_filter_movie_reject_result():
    dummy_search_result = SearchResult.parse('Titanic', 'https://dummy_page.com/films')
    assert MovieSearchEngine._filter_movie_service_result(dummy_search_result) == False
