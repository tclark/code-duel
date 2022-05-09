from collections import namedtuple

NAME = 'Rock Paper Scissors'
Result = namedtuple('Result', ['winner','loser'])

def _rock(opponent):
    if opponent == 'rock':
        return None
    if opponent == 'paper':
        return 1
    if opponent == 'scissors':
        return 0
    return None    

def _paper(opponent):
    if opponent == 'rock':
        return 0
    if opponent == 'paper':
        return None
    if opponent == 'scissors':
        return 1
    return None    

def _scissors(opponent):
    if opponent == 'rock':
        return 1
    if opponent == 'paper':
        return 0
    if opponent == 'scissors':
        return None
    return None    

evaluators = { 'rock': _rock, 'paper': _paper, 'scissors': _scissors}

class Game:

    def __init__(self, player0, player1):
        self._player = player0, player1
        self._scores = [0, 0]

    def _turn(self):
        result = None
        while result is None:
            result = self._evaluate_turn()
        self._scores[result] += 1
      
    def _evaluate_turn(self):
        p0_throw = self._player[0].play()
        p1_throw = self._player[1].play()
        self._player[0].notify(p1_throw)
        self._player[1].notify(p0_throw)
        return evaluators[p0_throw](p1_throw)

    def run(self):
        self._player[0].start_game()
        self._player[1].start_game()
        for _ in range(101):
            self._turn()
        if self._scores[0] >= 51:
            return Result(*self._player)
        return Result(*self._player[::-1])    
