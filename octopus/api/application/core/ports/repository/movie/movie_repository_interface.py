from abc import ABC, abstractmethod

from api.application.core.domain.movie.movie_entity import MovieEntity


class MovieRepositoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create(movie: MovieEntity):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_all_movies() -> list[MovieEntity]:
        raise NotImplementedError
