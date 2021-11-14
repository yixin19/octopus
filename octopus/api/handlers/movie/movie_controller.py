from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.application.core.service.movie.movie_service import MovieService
from api.handlers.movie.serializer.movie_serializer_input import MovieSerializerInput
from api.infrastructure.movie.repository.movie_repository import MovieRepository


class MovieController(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.movie_service = MovieService(movie_repository=MovieRepository())

    def post(self, request):
        try:
            serializer = MovieSerializerInput(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({}, status=status.HTTP_201_CREATED)
        except Exception as exception:
            return Response(str(exception), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        pass
