from django import forms

class GameForm(forms.Form):
    game = forms.CharField(label='Your name', max_length=100)