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
    associated with the game
    '''
    game = models.CharField(max_length=6)  #game will provide the unique id to the game

    def __str__(self):
        return self.game


class Player(models.Model):
    '''
    A player belongs to a game, for simplicity a player can only play one game at once.
    A player has a set of cards
    '''
    name = models.CharField(max_length=32)
    wins = models.IntegerField(blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WhiteCard(models.Model):
    '''The White cards of the Game  '''
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class BlackCard(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class Turn(models.Model):
    ''' '''
    decider = models.ForeignKey(Player, related_name="picker" ,on_delete=models.CASCADE)

    def __str__(self):
        return self.decider
