from film_details_searcher.scrappers.custom_headers import CUSTOM_HEADERS


def test_if_custom_headers_exists():
    assert CUSTOM_HEADERS is not None
    assert isinstance(CUSTOM_HEADERS, dict)


def test_custom_header_contains_user_agent_header():
    assert CUSTOM_HEADERS["User-Agent"] is not None
    assert CUSTOM_HEADERS["User-Agent"] != ''