import random


class Player:
    def __init__(self):
        self.player_name = __name__.split('.')[-1]

    def __str__(self):
        return self.player_name

    def play(self):
        return random.choice(('rock', 'paper', 'scissors'))

    def notify(self, opponent_throw):
        pass

    def start_game(self):
        pass
