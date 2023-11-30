# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Description: represent movies, manage their catalog in streaming services, and guide users to find which service streams a particular movie.

class Movie:
    """Represents a movie with title, genre, director, and year."""

    def __init__(self, title, genre, director, year):
        """Initialize the Movie with title, genre, director, and year."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Return the title of the movie."""
        return self._title

    def get_genre(self):
        """Return the genre of the movie."""
        return self._genre

    def get_director(self):
        """Return the director of the movie."""
        return self._director

    def get_year(self):
        """Return the year of the movie."""
        return self._year


class StreamingService:
    """Represents a streaming service with a name and a catalog of movies."""

    def __init__(self, name):
        """Initialize the StreamingService with a name."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Return the name of the streaming service."""
        return self._name

    def get_catalog(self):
        """Return the catalog of movies."""
        return self._catalog

    def add_movie(self, movie):
        """Add a movie to the catalog."""
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """Remove a movie from the catalog by title."""
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    """Represents a guide for streaming services."""

    def __init__(self):
        """Initialize the StreamingGuide with an empty list of streaming services."""
        self._streaming_services = []

    def add_streaming_service(self, service):
        """Add a streaming service to the guide."""
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        """Remove a streaming service from the guide by name."""
        self._streaming_services = [s for s in self._streaming_services if s.get_name() != name]

    def where_to_watch(self, title):
        """Return a list of streaming services where the movie is available."""
        for service in self._streaming_services:
            if title in service.get_catalog():
                movie = service.get_catalog()[title]
                services_showing = [s.get_name() for s in self._streaming_services if title in s.get_catalog()]
                return [f"{movie.get_title()} ({movie.get_year()})"] + services_showing
        return None
