from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxValueValidator,MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.DecimalField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.1)],
        decimal_places=1,
        max_digits=2
    )
    #stars = models.IntegerField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    review = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)