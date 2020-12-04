import pytest

from film_details_searcher.models.search_result import SearchResult
from film_details_searcher.models.select_menu import SelectMenu


@pytest.fixture
def empty_select_menu():
    """Returns empty SelectMenu"""
    return SelectMenu([])


@pytest.fixture
def sample_select_menu():
    """Returns sample SelectMenu"""
    movies_names = ['Titanic', 'Green Book', "Green mile"]
    menu_items = map(lambda x: SearchResult.parse(x, x), movies_names)
    return SelectMenu(menu_items)


def test_creation_of_empty_select_menu(empty_select_menu):
    assert empty_select_menu is not None


def test_str_of_empty_select_menu(empty_select_menu):
    assert str(empty_select_menu) == ''


def test_str_of_sample_select_menu(sample_select_menu):
    expected = "1. Movie title: Titanic\n2. Movie title: Green Book\n3. Movie title: Green mile"
    assert str(sample_select_menu) == expected


def test_all_menu_items_will_show(sample_select_menu):
    assert 3 == len(sample_select_menu.get_menu_items())