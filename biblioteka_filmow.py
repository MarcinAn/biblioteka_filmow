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
        super().__init__(title, release_year, genre, views)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"


def add_item(item, media_list):
    media_list.append(item)


def get_movies(media_list):
    movies = []
    for item in media_list:
        if type(item) is Movie:
            movies.append(item)
    movies = sorted(movies, key=lambda x: x.title)
    return movies


def get_series(media_list):
    series = []
    for serie in media_list:
        if type(item) is Series:
            series.append(serie)
    series = sorted(series, key=lambda x: x.title)
    return series


def search(title, media_list):
    for item in media_list:
        if title.lower() in item.title.lower():
            return item


def generate_views(media_list):
    views = random.randint(1, 100)
    list_nr = random.randint(0, len(media_list) - 1)
    item = media_list[list_nr]
    item.views += views


def play(title, media_list):
    item = search(title, media_list)
    item.views += 1


def generate_multiple_views(media_list):
    for _ in range(10):
        generate_views(media_list)


def top_titles(num_titles, media_list, content_type=None):
    if not content_type:
        items = media_list
    else:
        if content_type == "movie":
            items= get_movies(media_list)
        elif content_type == "series":
            items= get_series(media_list)
    items = sorted(items, key=lambda x: x.views, reverse=True)
    return items[:num_titles]


def create_movie(title, release_year, genre, views):
    return Movie(title, release_year, genre, views)


def create_series(title, release_year, genre, season, episode, views):
    return Series(title, release_year, genre, season, episode, views)


if __name__ == "__main__":

    media_items = []

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
    generate_multiple_views(media_items)

    # Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {current_date}")

    # Wyświetli listę top 3 najpopularniejszych tytułów.
    for item in top_titles(3, media_items):
        print(item)
