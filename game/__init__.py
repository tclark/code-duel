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
        self._players = (player0, player1)
        self._scores = [0, 0]

    def _turn(self):
        result = None
        while result is None:
            result = self._evaluate_turn(self._players[0].play(), self._players[1].play())
        self._scores[result] += 1
      
    def _evaluate_turn(self, p0, p1): 
        return evaluators[p0](p1)

    def run(self):
        for _ in range(3):
            self._turn()
        if self._scores[0] >= 2:
            return Result(*self._players)
        return Result(*self._players[::-1])    
