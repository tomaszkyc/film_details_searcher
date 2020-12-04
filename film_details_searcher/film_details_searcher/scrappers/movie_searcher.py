from film_details_searcher.models.select_menu import SelectMenu
from film_details_searcher.scrappers.filmweb_movie_service import FilmwebMovieService
from film_details_searcher.scrappers.google_movie_search_engine import GoogleMovieSearchEngine


class MovieSearcher:
    def __init__(self):
        pass

    def search(self, movie_title=''):
        if movie_title == '':
            movie_title = MovieSearcher._prompt_user_for_movie_title()
        movie_search_engine = GoogleMovieSearchEngine()
        print(f'Searching for movie: {movie_title}. Please wait...')
        search_results = movie_search_engine.search(movie_title)
        movie = None
        movie_service = FilmwebMovieService()
        if len(search_results) == 1:
            print('There is only one result. Skipping choice of movie search result.')
            link_to_movie = search_results[0].link()
            movie = movie_service.get_movie(link_to_movie)
        elif len(search_results) > 1:
            select_menu = MovieSearcher._build_select_menu(search_results)
            selected_item = select_menu.show_menu_and_wait_for_result()
            link_to_movie = selected_item.link()
            movie = movie_service.get_movie(link_to_movie)
        return movie

    @staticmethod
    def _prompt_user_for_movie_title():
        search_term = input("Type movie title you want to see details: ")
        return search_term

    @staticmethod
    def _build_select_menu(menu_items):
        select_menu = SelectMenu(menu_items)
        return select_menu
