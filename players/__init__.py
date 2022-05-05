import importlib
import os

players = []
with os.scandir(os.path.dirname(__file__)) as thisdir:
    for thing in thisdir:
        if os.path.isdir(thing) and thing.name[:2] != '__':
            players.append(importlib.import_module(f'.{thing.name}', 'players'))
            
