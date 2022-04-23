from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from toys.models import Toy
from toys.serializers import ToySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True, context={'request': request})
        return Response(toys_serializer.data)
    elif request.method == 'POST':
        toy_serializer = ToySerializer(data=request.data, context={'request': request})
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class ToyList(APIView):

    def get(self, request):
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True, context={'request': request})
        return Response(toys_serializer.data)

    def post(self, request):
        toy_serializer = ToySerializer(data=request.data, context={'request': request})
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy, context={'request': request})
        return Response(toy_serializer.data)
    elif request.method == 'PUT':
        toy_serializer = ToySerializer(toy, data=request.data, context={'request': request})
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        toy_serializer = ToySerializer(toy, data=request.data, context={'request': request}, partial=True)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class ToyDetail(APIView):

    def find_toy(self, pk):
        try:
            return Toy.objects.get(pk=pk)
        except Toy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        toy = Toy.objects.get(pk=pk)
        toy_serializer = ToySerializer(toy, context={'request': request})
        return Response(toy_serializer.data)

    def put(self, request, pk):
        toy = Toy.objects.get(pk=pk)
        toy_serializer = ToySerializer(toy, data=request.data, context={'request': request})
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        toy = Toy.objects.get(pk=pk)
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        toy = Toy.objects.get(pk=pk)
        toy_serializer = ToySerializer(toy, data=request.data, context={'request': request}, partial=True)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ToyViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
