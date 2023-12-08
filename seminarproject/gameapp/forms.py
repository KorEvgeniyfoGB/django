from django import forms


class GameCoinform(forms.Form):
    game = forms.ChoiceField(choices=(('coin', 'Монетка'), ('dice', 'Кости'), ('number', 'Случайное число')))
    size = forms.IntegerField(min_value=1, max_value=50)


