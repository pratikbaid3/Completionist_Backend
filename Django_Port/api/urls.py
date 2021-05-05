from django.urls import path

from api.views import Ps4GamesView, Ps4GameView, Ps4GamesGuideView

app_name = 'api'

urlpatterns = [
    path('ps4/games/', Ps4GamesView.as_view(), name='games list'),
    path('ps4/game/<str:game_name>', Ps4GameView.as_view(), name='game'),
    path('ps4/guide/<str:game_name>',Ps4GamesGuideView.as_view(),name='guide')
]
