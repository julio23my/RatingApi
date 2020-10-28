from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import RatingSerializer,MovieSerializer, UserSerializer,ListSerializer
from .models import Movie, RatingMovie,Lista
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    @action(detail=True,methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'points' in request.data:

            movie = Movie.objects.get(pk=pk)
            points = request.data['points']
            user = request.user
            print('movie title', movie.title)
            print('username:', user)

            try:
                rating = RatingMovie.objects.get(user=user.id, movie=movie.id)
                rating.points = points
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'RatingMovie Update','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = RatingMovie.objects.create(user=user, movie=movie, points=points)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'RatingMovie Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     response = {'message': 'You cant update rating like that '}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     response = {'message': 'You cant create movies like that '}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingMovie.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that '}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that '}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)