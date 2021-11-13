from rest_framework.views import APIView

from api.application.core.service.movie.movie_service import MovieService
from api.infrastructure.movie.repository.movie_repository import MovieRepository


class MovieController(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, request, *args, **kwargs):
        super().setup(*args, **kwargs)
        self.movie_service = MovieService(movie_repository=MovieRepository())

    def post(self):
        pass
