""" This
      1. Scans the directory for player submodule directories
      2. Imports the submodules
      3. Populates a list with those submodules that importers can use to
         get the modules and their Player classes.
"""


import importlib
import os

player_modules = []
with os.scandir(os.path.dirname(__file__)) as thisdir:
    for thing in thisdir:
        if os.path.isdir(thing) and thing.name[:2] != '__':
            player_modules.append(importlib.import_module(
                f'.{thing.name}', 'players'))
