import pytest
from film_details_searcher.models.search_result import SearchResult
from dataclasses import FrozenInstanceError

example_film_title = 'Titanic'
example_film_link = 'google.com'


@pytest.fixture
def empty_search_result():
    """Returns an empty SearchResult"""
    return SearchResult.parse('', '')


@pytest.fixture
def example_search_result():
    """Returns an SearchResult with sample data"""
    return SearchResult.parse(example_film_title, example_film_link)


def test_operations_on_title(example_search_result):
    assert example_search_result.title() == example_film_title


def test_operations_on_link(example_search_result):
    assert example_search_result.link() == example_film_link


def test_parse_fetched_film_title():
    search_result = SearchResult.parse('Titanic - Filmweb', '')
    assert search_result.title() == 'Titanic'


def test_read_only_values_in_search_results(example_search_result):
    with pytest.raises(FrozenInstanceError):
        example_search_result.details = dict()


def test_parsing_some_data_to_search_result():
    search_result = SearchResult.parse(example_film_title, example_film_link)
    assert search_result is not None
    assert search_result.link() == example_film_link
    assert search_result.title() == example_film_title


def test_empty_search_result(empty_search_result):
    assert empty_search_result.link() == ''
    assert  empty_search_result.title() == ''


def test_invalid_arguments_shoud_raises_an_exception():
    with pytest.raises(TypeError) as e:
        SearchResult.parse([], '')

    with pytest.raises(TypeError) as e:
        SearchResult.parse('', [])