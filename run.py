#! /usr/bin/env python3

from players import player_modules
from game import Game, NAME
from random import randint, shuffle


def insert_bye(player_list):
    if len(player_list) % 2 == 1:
        # Stick a None in there to set up a bye
        player_list.insert(randint(0, len(player_list)), None)


def handle_bye(p1, p2):
    if p1 is None:
        winner = p2
    else:
        winner = p1
    print(f'{winner} gets a bye')
    return winner


def play_round(active_players, rnd):
    print(f'\nRound {rnd}')
    if len(active_players) == 2:
        print('FINAL ROUND')
    advances = []    
    while active_players: 
        insert_bye(active_players)        
        p1 = active_players.pop()
        p2 = active_players.pop()
        if p1 is None or p2 is None:
            advances.append(handle_bye(p1, p2))
        else:
            print(f'{p1} vs. {p2}')
            g = Game(p1, p2)
            result = g.run()
            print(f'{result.winner} advances\n')
            advances.append(result.winner)
    return advances[::-1]        
            

players = [p.Player() for p in player_modules]
shuffle(players)
tournament_round = 1

print(f'Playing: {NAME}')
print('The players are:')
for p in players:
    print(f'  {p}')
while len(players) > 1:
    players = play_round(players, tournament_round)
    tournament_round += 1
print(f'Final winner: {players[0]}')
    
