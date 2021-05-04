from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.PS4Game)
class PS4GameAdmin(admin.ModelAdmin):
    list_display = [
        'game_name',
        'gold',
        'silver',
        'bronze',
        'platinum'
    ]


@admin.register(models.PS4GamesGuide)
class PS4GameAdmin(admin.ModelAdmin):
    list_display = [
        'game_name',
        'trophy_name',
        'trophy_type'
    ]
