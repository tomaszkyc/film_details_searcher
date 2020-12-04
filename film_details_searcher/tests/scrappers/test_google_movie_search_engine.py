import pytest

from film_details_searcher.scrappers.google_movie_search_engine import GoogleMovieSearchEngine


@pytest.fixture
def google_movie_search_engine():
    return GoogleMovieSearchEngine()


def test_raises_an_exception_if_movie_title_is_not_str(google_movie_search_engine: GoogleMovieSearchEngine):
    with pytest.raises(TypeError) as e:
        google_movie_search_engine.search([])


def test_search_movie_in_search_engine_and_returns_results(google_movie_search_engine: GoogleMovieSearchEngine):
    search_results = google_movie_search_engine.search('Titanic')
    assert search_results is not None
    assert len(search_results) != 0


def test_search_movie_in_search_engine_and_return_results_with_private_method(
        google_movie_search_engine: GoogleMovieSearchEngine):
    search_results = google_movie_search_engine._do_search('Titanic')
    assert search_results is not None
    assert len(search_results) != 0
