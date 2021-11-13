from rest_framework.test import APITestCase


class TestCreateMovie(APITestCase):
    def setUp(self):
        self.movie_url = "/api/movie/"
