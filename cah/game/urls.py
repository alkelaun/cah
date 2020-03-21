
from django.urls import path
from .views import index, register, game, players_hand, turn

urlpatterns = [
    path('', index, name="home"),
    path('register', register, name="register"),
    path('game/<id>', game, name="game"),
    path('hand', players_hand, name="hand"),
    path('turn', turn, name="turn"),
    
    path('about', index, name="about"),
    path('account_signup', index, name="account_signup"),
    path('account_login', index, name="account_login"),
]