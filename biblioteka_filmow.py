from datetime import datetime
import random


class Movie:
    def __init__(self, title, release_year, genre, views):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Series(Movie):
    def __init__(self, title, release_year, genre, season, episode, views):
        Movie.__init__(self, title, release_year, genre, views)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"


def add_item(item, media_list):
    media_list.append(item)


def get_movies(media_list):
    movies = []
    for item in media_list:
        if isinstance(item, Movie) and not isinstance(item, Series):
            movies.append(item)
    movies = sorted(movies, key=lambda x: x.title)
    return movies


def get_series(media_list):
    series = []
    for serie in media_list:
        if isinstance(serie, Series):
            series.append(serie)
    series = sorted(series, key=lambda x: x.title)
    return series


def search(title, media_list):
    for item in media_list:
        if title.lower() in item.title.lower():
            return item


def generate_views(title, media_list):
    views = random.randint(1, 100)
    item = search(title, media_list)
    item.views += views


def play(title, media_list):
    item = search(title, media_list)
    item.views += 1


def generate_multiple_views(title, media_list):
    for i in range(10):
        generate_views(title, media_list)


def top_titles(num_titles, media_list, content_type=None):
    if content_type == None:
        items = sorted(media_list, key=lambda x: x.views, reverse=True)
    else:
        if content_type == "movie":
            content = Movie
        elif content_type == "series":
            content = Series
        items = []
        for item in media_list:
            if isinstance(item, content):
                items.append(item)
        items = sorted(items, key=lambda x: x.views, reverse=True)
    return items[:num_titles]


def create_movie(title, release_year, genre, views):
    return Movie(title, release_year, genre, views)


def create_series(title, release_year, genre, season, episode, views):
    return Series(title, release_year, genre, season, episode, views)


media_items = []

if __name__ == "__main__":

    # Wyświetli na konsoli komunikat Biblioteka filmów.
    print("Biblioteka filmów")

    # Wypełni bibliotekę treścią.
    add_item(create_movie("The Shawshank Redemption", 1994, "Drama", 0), media_items)
    add_item(create_movie("Pulp Fiction", 1994, "Crime", 0), media_items)
    add_item(create_movie("The Green Mile", 1999, "Drama", 0), media_items)
    add_item(
        create_series("Stranger Things", 2016, "Science Fiction", 1, 1, 0), media_items
    )
    add_item(create_series("Game of Thrones", 2011, "Fantasy", 3, 5, 0), media_items)
    add_item(create_series("Narcos", 2015, "Thriller", 1, 3, 0), media_items)

    # Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
    for item in media_items:
        generate_views(item.title, media_items)

    # Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {current_date}")

    # Wyświetli listę top 3 najpopularniejszych tytułów.
    for item in top_titles(3, media_items):
        print(item)
