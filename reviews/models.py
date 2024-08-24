from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.PROTECT,
                              related_name='reviews'
                              )
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'The value must be greater than 0 stars.'),
        MaxValueValidator(5, 'The value must be less than 5 stars.')
        ])
    comment = models.CharField(max_length=1000,
                               blank=True,
                               null=True)

    def __str__(self):
        return f"Review of {self.movie.title} - {self.stars} stars"