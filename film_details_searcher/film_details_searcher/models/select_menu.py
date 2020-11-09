import sys


class SelectMenu:
    def __init__(self, search_results):
        self._search_results = search_results

    def __str__(self):
        return str(self._search_results)

    def _display_menu_items(self):
        for index, search_result in enumerate(self._search_results, start=1):
            print(f"{index}. Film title: {search_result.title}")

    def show_menu_and_wait_for_result(self):
        while True:
            print("Select which film details want to show:")
            self._display_menu_items()
            try:
                selected_option = int(input("Choose number of film to show details: "))
                if selected_option < 1 or selected_option > len(self._search_results):
                    raise ValueError(f"Incorrect number. Choose in range from 1 to {len(self._search_results)}")
                return self._search_results[selected_option - 1]  # minus 1 cause list is indexed from 1
            except ValueError as e:
                print(e)
