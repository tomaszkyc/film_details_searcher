# Film Details Searcher
`film_details_searcher` is a small tool to search film details right from the command line.  
It use a polish movie online website [Filmweb](https://filmweb.pl) and [Google](https://google.com)  

![](resources/images/usage.gif)

Designed for people who don't want to open web browser and search for film description.

**Libraries used**
---
1. [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - Python web scrapping library
2. [Requests](https://requests.readthedocs.io/en/master/) - library for making HTTP requests
3. [pytest](https://docs.pytest.org/en/stable/) - for tests purposes
4. [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) - for test coverage checking

**Usage**
---
```bash
$ python film_details_searcher

    After that you will be prompt for film title
```

```bash
$ python film_details_searcher <put_here_film_title>

    After that application will start searching  
    given movie title without prompting for title
```

**Instalation options**
---

1. Make sure you're using Python 3.6 or higher.
2. Run
```bash
pip install -r requirements.txt
```

**Changelog**
---

Project contains [changelog](CHANGELOG.md). Visit it if you want to check more details.

**How to Contribute**
---

1. Clone repo and create a new branch: `$ git checkout https://github.com/tomaszkyc/film_details_searcher -b name_for_new_branch`.
2. Make changes and add required tests
3. Make sure that all tests pass:
```bash
pytest --cov-report  term-missing --cov=film_details_searcher/film_details_searcher
```
3. Submit Pull Request with comprehensive description of changes

**Acknowledgements**
---
1. I'm using scrapping only for learning purposes and project demo. You sould not  
   do it in your production code.
   
**Donations**
---

This is free, open-source software. No need to pay for it or donate.