from rest_framework import serializers
from IMDB_APP.models import Actor
from IMDB_APP.models import Director
from IMDB_APP.models import Movie


class ActorMovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'url']


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    movies = ActorMovieSerializer(many=True)
    class Meta:
        model = Actor
        fields = ['url', 'pk', 'name', 'birthday', 'description', 'movies']


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['url', 'pk', 'name', 'birthday', 'description']


class MovieActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'url']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = MovieActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['url', 'pk', 'name', 'description', 'movie_category', 'release_date', 'actors']
