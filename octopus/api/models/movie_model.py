from django.db import models


class MovieModel(models.Model):
    title = models.CharField(max_length=512)
    release_date = models.DateTimeField()

    class Meta:
        db_table = "movie"
