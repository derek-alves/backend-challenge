from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ViewSet):
    def list(self, request):
        places = Place.objects.order_by('name')
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Place.objects.all()
        place = get_object_or_404(queryset, pk=pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Place.objects.all()
        place = get_object_or_404(queryset, pk=pk)
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            place = PlaceSerializer().update(instance=place, validated_data=request.data)
            serializer = PlaceSerializer(place)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Place.objects.all()
        place = get_object_or_404(queryset, pk=pk)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
