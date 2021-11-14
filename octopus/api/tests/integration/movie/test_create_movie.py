from datetime import datetime

from rest_framework.test import APITestCase

from api.models.movie_model import MovieModel


class TestCreateMovie(APITestCase):
    def setUp(self):
        self.movie_url = "/api/movie/"

    def test_post_movie_and_movie_is_created(self):
        # Given
        post_data = {"title": "test_title", "release_date": "2021-01-01 00:00:00"}

        # Then
        self.client.post(self.movie_url, data=post_data, format="json")

        # Then
        created_movie = MovieModel.objects.all()[0]
        self.assertEqual(created_movie.title, post_data["title"])
        self.assertEqual(
            datetime.strftime(created_movie.release_date, "%Y-%m-%d %H:%M:%S"),
            post_data["release_date"],
        )
