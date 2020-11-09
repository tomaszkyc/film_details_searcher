import time


class FilmDetails:
    def __init__(self, title, description, premiere_year, film_time, film_rating_value, film_rating_count):
        self._title = title
        self._description = description
        self._premiere_year = premiere_year
        self._film_time = self._parse_film_time(film_time)
        self._film_rating_value = film_rating_value
        self._film_rating_count = self._parse_film_rating_count(film_rating_count)

    def __str__(self):
        return f"Title: {self._title}\nDescription (PL only): {self._description}\nPremiere year: {self._premiere_year} " \
               f"\nRunning time: {self._film_time}\nFilm rating value: {self._film_rating_value}" \
               f"\nNumber of votes: {self._film_rating_count}"

    def _parse_film_time(self, fetched_film_time):
        for time_format in ("%H godz. %M min.", '%H godz.', "%M min."):
            try:
                parsed_time = time.strptime(fetched_film_time, time_format)
                return time.strftime("%Hh %Mmin", parsed_time)
            except ValueError:
                pass
        return "n/a"

    def _parse_film_rating_count(self, film_rating_count):
        return film_rating_count.replace('  oceny', '').replace('  ocen', '')
