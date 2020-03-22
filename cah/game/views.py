from django.shortcuts import render, redirect

import random, string

# Create your views here.
def create_new_room():
    room = ''.join(random.choices(string.ascii_letters, k = 6)).upper() # 6 character room name e.g. ZXYDEF
    return room

def index(request):

    if request.method == 'POST':
        if request.POST.get('gamecode', False):
            room = request.POST['gamecode']
        else:
            room = create_new_room()
        return redirect('gameroom', id=room)
    '''
    Provides an option to create a new game or join an already started game
    '''

    return render(request, "game/base.html")

def register(request):
    ''' From the game, redirect to this page to enter a name'''
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

def players_hand(request, id, name):
    '''
    Displays the players hand
    Black card currently being played
    Seven white cards
    '''
    return render(request, "game/players_hand.html", {'id':id})


