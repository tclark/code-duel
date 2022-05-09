import random


class Player:
    def __init__(self):
        self.player_name = __name__.split('.')[-1]
        self._opponent_throws = []
        

    def __str__(self):
        return self.player_name

    def play(self):
        if not self._opponent_throws:
            return random.choice(('rock', 'paper', 'scissors'))
        else:
            return self._optimal()

    def notify(self, opponent_throw):
        self._opponent_throws.append(opponent_throw)

    def start_game(self):
        self._opponent_throws = []

    def _optimal(self):
        counts = {}
        counts[self._opponent_throws.count('rock')] = 'paper'
        counts[self._opponent_throws.count('paper')] = 'scissors'
        counts[self._opponent_throws.count('scissors')] = 'rock'
        return counts[max(counts.keys())]
