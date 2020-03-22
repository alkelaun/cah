
from django.urls import path
from .views import index, register, game, players_hand, turn

urlpatterns = [
    path('', index, name="home"),
    path('register', register, name="register"),
    path('game/<id>', game, name="gameroom"),  #game board
    path('game/<id>/<name>', players_hand, name="hand"), #on phone
    path('turn', turn, name="turn"),

    path('about', index, name="about"),
    path('account_signup', index, name="account_signup"),
    path('account_login', index, name="account_login"),
]