from dataclasses import dataclass


@dataclass(init=True, repr=True, eq=True, frozen=True)
class SearchResult:
    details: dict

    @classmethod
    def parse(cls, title, link):
        if not isinstance(title, str) or not isinstance(link, str):
            raise TypeError('Link and title should be str type')
        title = SearchResult._parse_title(title)
        attr = {"title": title, "link": link}
        return cls(attr)

    def link(self):
        return self.details['link']

    def title(self):
        return self.details['title']

    @staticmethod
    def _parse_title(title):
        return title.replace(' - Filmweb', '')
