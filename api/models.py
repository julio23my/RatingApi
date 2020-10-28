from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxValueValidator,MinValueValidator
from positions.fields import PositionField


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title

    def no_of_ratings(self):
        ratings = RatingMovie.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        ratings = RatingMovie.objects.filter(movie=self)
        sum = 0
        for rating in ratings:
            sum+= rating.points
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0



class RatingMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.DecimalField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.1)],
        decimal_places=1,
        max_digits=2
    )
    review = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)


class Anime(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manga(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lista(models.Model):
    name = models.CharField(max_length=60)
    movies = models.ManyToManyField('Movie', through='ListMovie', related_name='movies',blank=True)
    animes = models.ManyToManyField('Anime', through='ListAnime', related_name='animes',blank=True)
    books = models.ManyToManyField('Book', through='ListBook', related_name='books',blank=True)
    mangas = models.ManyToManyField('Manga', through='ListManga', related_name='mangas',blank=True)


    def __str__(self):
        return self.name

    def completmovie(self):
        queryset = ListMovie.objects.filter(lista=self.pk)
        return queryset

class ListMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    position = PositionField(collection='lista')

    class Meta:
        unique_together = ('movie','lista')
    def __str__(self):
        return self.lista.name

class ListAnime(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    position = PositionField(collection='lista')

    class Meta:
        unique_together = ('anime','lista')


    def __str__(self):
        return self.lista.name

class ListManga(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    position = PositionField(collection='lista')

    class Meta:
        unique_together = ('manga','lista')


class ListBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    position = PositionField(collection='lista')

    class Meta:
        unique_together = ('book','lista')