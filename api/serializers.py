from rest_framework import serializers
from .models import Movie,RatingMovie, Lista, ListMovie, Manga, Book, Anime, ListAnime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields= ['id','title','description','no_of_ratings','avg_rating']


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manga
        fields= ['id','name']


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Anime
        fields= ['id','name','author']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= RatingMovie
        fields= ['id','points','user','movie']


class ListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    animes = AnimeSerializer(many=True, read_only=True)
    mangas = MangaSerializer(many=True, read_only=True)
    class Meta:
        model= Lista
        fields= ['id','name', 'movies','animes','mangas']

