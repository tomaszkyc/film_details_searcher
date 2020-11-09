class SearchResult:

    def __init__(self, title, link):
        self._title = self._parse_title(title)
        self._link = link

    def __str__(self):
        return f"Page title: {self.title} page link: {self.link}"

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    @classmethod
    def parse(cls, title, link):
        return cls(title, link)

    def _parse_title(self, title):
        return title.replace(' - Filmweb', '')
