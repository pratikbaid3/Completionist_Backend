from rest_framework import serializers
from .models import Ps4Games, Ps4GamesGuide


class Ps4GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ps4Games
        fields = '__all__'


class Ps4GamesGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ps4GamesGuide
        fields = '__all__'
