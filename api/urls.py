
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet,RatingViewSet, UserViewSet,ListaViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movie', MovieViewSet)
router.register('rating', RatingViewSet)
router.register('lista', ListaViewSet)


urlpatterns = [
    path('', include(router.urls)),

]