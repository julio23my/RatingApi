from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import RatingSerializer,MovieSerializer
from .models import Movie, Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True,methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'points' in request.data:

            movie = Movie.objects.get(pk=pk)
            points = request.data['points']
            # user = request.user
            user = User.objects.get(pk=1)
            print('movie title', movie.title)
            print('username:', user.username)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.points = points
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Update','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user,movie=movie, points=points)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)



        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer