from abc import ABC, abstractmethod

from api.application.core.domain.movie.movie_entity import MovieEntity


class MovieRepositoryInterface(ABC):
    @abstractmethod
    def create(self, movie: MovieEntity):
        raise NotImplementedError

    @abstractmethod
    def get_all_movies(self) -> list[MovieEntity]:
        raise NotImplementedError
