from django.db import models

# Create your models here.
'''
Cards Against Humanity:
 - Game
 - Players
 - Turn (Either a Turn or an Evaluator needs to be part of the game)
 - Evaluator (rotates)
 - White Cards
 - Black Cards
'''

class Game(models.Model):
    '''
    '''
    game = models.CharField(max_length=4)  #game will provide the unique id to the game


class Player(models.Model):
    '''
    A player belongs to a game, for simplicity a player can only play one game at once.
    A player has a set of cards
    '''
    name = models.CharField(max_length=32)
    wins = models.IntegerField()

    def __str__(self):
        return self.name

class WhiteCard(models.Model):
    '''The White cards of the Game  '''

class Turn(models.Model):
    ''' '''
    decider = models.ForeignKey(Player, on_delete=models.CASCADE)
