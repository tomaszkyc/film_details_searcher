import pytest

from film_details_searcher.models.movie import Movie

movie_details = {"title": "Titanic", "description_pl": "Titanic wyrusza w swój dziewiczy rejs. Wśród pasażerów "
                                                       "statku są: młody chłopak ze skradzionym biletem, "
                                                       "zamężna arystokratka wracająca z pogrzebu ciotki i "
                                                       "opiekunka do dzieci o tajemniczej przeszłości.",
                 "premiere_year": "1996", "movie_time": "2 godz. 53 min.",
                 "movie_rating_value": "7,3", "movie_rating_count": "27604"}


@pytest.fixture
def example_movie():
    """Returns a example Movie object"""
    return Movie.parse(movie_details)


def test_should_parse_all_film_details():
    movie = Movie.parse(movie_details)
    assert len(movie.details) == 6


@pytest.mark.parametrize("given_key, expected_value, expected_result", [
    ("title", "Titanic", True),
    ("premiere_year", "1996", True),
    ("movie_time", "02h 53min", True),
    ("movie_time", "2 godz. 53 min.", False),
    ("movie_rating_value", "00", False),
    ("movie_rating_value", "7,3", True),
    ("movie_rating_count", "27604", True),
    ("description_pl", "TEST", False)
])
def test_should_get_some_film_details(example_movie: Movie, given_key, expected_value, expected_result):
    value_from_movie = example_movie.details[given_key]
    assert (value_from_movie == expected_value) == expected_result


def test_should_parse_properly_time():
    parsed_time = Movie._parse_movie_time('02h 53min')
    assert parsed_time == '02h 53min'


def test_should_parse_nonparable_time_to_na():
    parsed_time = Movie._parse_movie_time('test')
    assert parsed_time == 'n/a'


def test_should_parse_movie_rating_count():
    parsed_movie_rating_count = Movie._parse_movie_rating_count('123  oceny')
    assert parsed_movie_rating_count == '123'


def test_should_return_str_for_nonempty_movie(example_movie):
    assert str(example_movie) != ''
