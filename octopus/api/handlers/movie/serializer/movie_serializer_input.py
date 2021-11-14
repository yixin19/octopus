from rest_framework import serializers

from api.models.movie_model import MovieModel


class MovieSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ["title", "release_date"]
