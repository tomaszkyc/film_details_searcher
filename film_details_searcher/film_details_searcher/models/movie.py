import time
from dataclasses import dataclass


@dataclass(init=True, repr=True, eq=True, frozen=True)
class Movie:
    details: dict

    def __str__(self):
        print_values = {"title": "Title", "description_pl": "Description (PL only)", "premiere_year": "Premiere year",
                        "movie_time": "Running time", "movie_rating_value": "Movie rating value",
                        "movie_rating_count": "Number of votes:"}
        result = ''
        for key, value in print_values.items():
            result += f"{value}: {self.details.get(key, 'n/a')}\n"
        return result

    @classmethod
    def parse(cls, details):
        if 'description_pl' in details:
            details['description_pl'] = Movie._parse_movie_description(details['description_pl'])
        if 'movie_time' in details:
            details['movie_time'] = Movie._parse_movie_time(details['movie_time'])
        if 'movie_rating_count' in details:
            details['movie_rating_count'] = Movie._parse_movie_rating_count(details['movie_rating_count'])
        return cls(details)

    @staticmethod
    def _parse_movie_time(movie_time):
        for time_format in ("%H godz. %M min.", '%H godz.', "%M min.", "%Hh %Mmin"):
            try:
                parsed_time = time.strptime(movie_time, time_format)
                return time.strftime("%Hh %Mmin", parsed_time)
            except ValueError:
                pass
        return 'n/a'

    @staticmethod
    def _parse_movie_rating_count(film_rating_count):
        return film_rating_count.replace('  oceny', '').replace('  ocen', '')

    @staticmethod
    def _parse_movie_description(movie_description):
        return movie_description.replace('  dodaj fabułę', '')
