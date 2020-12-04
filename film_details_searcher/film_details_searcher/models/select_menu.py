class SelectMenu:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return '\n'.join(self.get_menu_items())

    def get_menu_items(self):
        menu_items = []
        for index, item in enumerate(self.items, start=1):
            menu_items.append(f"{index}. Movie title: {item.title()}")
        return menu_items

    def show_menu_and_wait_for_result(self):
        while True:
            print("Select which film details want to show:")
            menu_items = self.get_menu_items()
            for menu_item in menu_items:
                print(menu_item)
            try:
                selected_option = int(input("Choose number of film to show details: "))
                if selected_option < 1 or selected_option > len(self.items):
                    raise ValueError(f"Incorrect number. Choose in range from 1 to {len(self.items)}")
                return self.items[selected_option - 1]  # minus 1 cause list is indexed from 1
            except ValueError as e:
                print(e)
