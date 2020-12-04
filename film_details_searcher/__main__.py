from film_details_searcher.scrappers.movie_searcher import MovieSearcher
import sys


def _parse_input_args_as_movie_title():
    return ' '.join(sys.argv[1:])

def main():
    movie_title = _parse_input_args_as_movie_title()
    movie_searcher = MovieSearcher()
    movie = movie_searcher.search(movie_title)
    print(movie)


if __name__ == '__main__':
    main()
