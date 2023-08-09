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


class Actions:
    def __init__(self):
        self.media_items = []

    def add_item(self, item):
        self.media_items.append(item)

    def get_movies(self):
        movies = []
        for movie in self.media_items:
            if isinstance(movie, Movie):
                movies.append(movie)
        movies= sorted(movies, key=lambda x: x.title)
        return movies

    def get_series(self):
        series = []
        for serie in self.media_items:
            if isinstance(serie, Series):
                series.append(serie)
        series= sorted(series, key=lambda x: x.title)
        return series

    def search(self, title):
        for item in self.media_items:
            if title.lower() in item.title.lower():
                return item

    def generate_views(self, title):
        views = random.randint(1, 100)
        item = self.search(title)
        item.views += views
        return item
        
    def play(self, title):
        item = self.search(title)
        item.views += 1

    def generate_multiple_views(self):
        for item in range(10):
            self.generate_views()

    def top_titles(self, num_titles, content_type=None):

        if content_type == "movie":
            content = Movie
        elif content_type == "series":
            content = Series
        items = []
        for item in self.media_items:
            if isinstance(item, content):
                items.append(item)
        items= sorted(items, key=lambda x: x.views, reverse=True)
        items= items[:num_titles]
        return items


action = Actions()

movie1 = Movie("The Shawshank Redemption", 1994, "Drama", 0)
movie2 = Movie("Pulp Fiction", 1994, "Crime", 0)
series1 = Series("Stranger Things", 2016, "Science Fiction", 1, 1, 0)
series2 = Series("Game of Thrones", 2011, "Fantasy", 3, 5, 0)

action.add_item(movie1)
action.add_item(movie2)
action.add_item(series1)
action.add_item(series2)

print("Wyświetl listę filmów")
for movie in action.get_movies():
    print(movie)

print("Wyświetl listę seriali")
for serie in action.get_series():
    print(serie)

print("Znajdż tytuł")
print(action.search('game of thrones'))

print("Dodaj losową liczbę wyświetleń")
action.generate_views('Stranger Things')

print("Wyświetl top 1 serial")
for series in action.top_titles(1, 'series'):
    print(series)