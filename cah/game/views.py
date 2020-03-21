from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Provides an option to create a new game or join an already started game
    '''
    return render(request, "game/base.html")

def register(request):
    ''' After joining a game, redirect to this page to enter a name'''
    return render(request, "game/register.html")

def game(request, id):
    '''
    Displays:
    Players and score
    Black Card
    Who's turn it is
    '''
    return render(request, "game/game.html", {'id':id})

def turn(request):
    '''Displays the deciders screen '''
    return render(request, "game/turn.html")


def white_card(request):
    '''
    Displays the white card
    '''

def players_hand(request):
    '''
    Displays the players hand
    Black card currently being played
    Seven white cards
    '''
    return render(request, "game/players_hand.html")


