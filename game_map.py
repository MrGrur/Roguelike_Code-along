import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

        self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x, y):
        """Returns True if x and y are inside the maps' bounds"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console):
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]