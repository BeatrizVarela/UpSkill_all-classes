from IMDB_APP.models import Actor, Director, Movie
from IMDB_APP.serializers import ActorSerializer, DirectorSerializer, MovieSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class ActorsViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class DirectorsViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class MoviesViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
