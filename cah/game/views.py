from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Provides an option to create a new game or join an already started game
    '''
    return render(request, "game/base.html")

def register(request):
    ''' After joining a game, redirect to this page to enter a name'''

def game(request):
    '''
    Displays:
    Players and score
    White Card
    Who's turn it is
    '''

def turn(request):
    '''Displays the deciders screen '''


def white_card(request):
    '''
    Displays the white card
    '''

def players_hand(request):
    '''
    Displays the players hand
    The white card currently being played
    And seven black cards
    '''


