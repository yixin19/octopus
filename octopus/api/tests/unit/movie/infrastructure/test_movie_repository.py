from datetime import datetime
from unittest.mock import patch

from django.test import SimpleTestCase
from pytz import utc

from api.application.core.domain.movie.movie_entity import MovieEntity
from api.infrastructure.movie.repository.movie_repository import MovieRepository
from api.models.movie_model import MovieModel


class TestMovieRepository(SimpleTestCase):
    def setUp(self):
        self.movie_entity_to_create = MovieEntity(
            title="title_test",
            release_date=datetime(2021, 1, 1, 0, 0, 0, tzinfo=utc),
        )
        self.movie_model_created = MovieModel(
            title=self.movie_entity_to_create.title,
            release_date=self.movie_entity_to_create.release_date,
        )
        self.movie_repository = MovieRepository()

    def test_create_movie_calls_create_in_models(self, *args):
        with patch.object(MovieModel.objects, "create") as create_mock:
            # Given
            create_mock.return_value = self.movie_model_created
            # When
            movie_entity_created = self.movie_repository.create(
                self.movie_entity_to_create
            )
            # Then
            self.assertEqual(movie_entity_created, self.movie_entity_to_create)
            create_mock.assert_called_once()
