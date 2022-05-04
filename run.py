#! /usr/bin/env python3

from players import alice, bob
from game import Game

a = alice.Player()
b = bob.Player()
g = Game(a, b)
w = g.run()
print(w)
