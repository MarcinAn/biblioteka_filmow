import random


class Media:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Info:
    def __init__(self, genre, views):
        self.genre = genre
        self.views = views

    def __str__(self):
        return f"{self.genre} ({self.views})"


class Movie(Media, Info):
    def __init__(self, title, release_year, genre, views):
        Media.__init__(self, title, release_year)
        Info.__init__(self, genre, views)

    def __str__(self):
        return super().__str__()


class Series(Media, Info):
    def __init__(self, title, release_year, genre, season, episode, views):
        Media.__init__(self, title, release_year)
        Info.__init__(self, genre, views)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"


media_items = []


def add_item(item, media_list):
    media_list.append(item)


def get_movies(media_list):
    movies = []
    for movie in media_list:
        if isinstance(movie, Movie):
            movies.append(movie)
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
    return item


def play(title):
    item = search(title)
    item.views += 1


def generate_multiple_views(title, media_list):
    for _ in range(10):
        generate_views(title, media_list)


def top_titles(num_titles, media_list, content_type=None):

    if content_type == "movie":
        content = Movie
    elif content_type == "series":
        content = Series
    items = []
    for item in media_list:
        if isinstance(item, content):
            items.append(item)
    items = sorted(items, key=lambda x: x.views, reverse=True)
    items = items[:num_titles]
    return items


def create_movie(title, release_year, genre, views):
    return Movie(title, release_year, genre, views)


def create_series(title, release_year, genre, season, episode, views):
    return Series(title, release_year, genre, season, episode, views)


add_item(create_movie("The Shawshank Redemption", 1994, "Drama", 0), media_items)
add_item(create_movie("Pulp Fiction", 1994, "Crime", 0), media_items)
add_item(
    create_series("Stranger Things", 2016, "Science Fiction", 1, 1, 0), media_items
)
add_item(create_series("Game of Thrones", 2011, "Fantasy", 3, 5, 0), media_items)

print("Wyświetl listę filmów")
for movie in get_movies(media_items):
    print(movie)

print("Wyświetl listę seriali")
for serie in get_series(media_items):
    print(serie)

print("Znajdż tytuł")
print(search("game of thrones", media_items))

print("Dodaj losową liczbę wyświetleń")
generate_views("Stranger Things", media_items)

print("Wyświetl top 1 serial")
for series in top_titles(1, media_items, "series"):
    print(series)
