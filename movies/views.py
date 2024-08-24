from django.shortcuts import render
from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer