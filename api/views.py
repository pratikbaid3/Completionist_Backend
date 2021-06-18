from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Ps4Games, Ps4GamesGuide
from api.serializers import Ps4GameSerializer, Ps4GamesGuideSerializer
from rest_framework import filters


class Ps4GamesView(generics.ListAPIView):  # Returns paginated list of games
    serializer_class = Ps4GameSerializer
    queryset = Ps4Games.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['game_name']


class Ps4GameView(APIView):  # Returns single game
    def get(self, request, format=None, **kwargs):
        game = Ps4Games.objects.get(game_name=kwargs['game_name'])
        serializer = Ps4GameSerializer(game)
        return Response({'results': serializer.data})


class Ps4GamesGuideView(APIView):  # Return game by game name
    def get(self, request, format=None, **kwargs):
        guide = Ps4GamesGuide.objects.filter(game_name=kwargs['game_name'])
        serializer = Ps4GamesGuideSerializer(guide, many=True)
        return Response({'result': serializer.data})
