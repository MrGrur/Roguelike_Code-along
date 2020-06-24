from typing import Tuple

import numpy as np


# Tile graphics struct (see: C++) type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Character represented
        ("fg", "3B"),  # foreground RGB colour tuple
        ("bg", "3B")  # background RGB colour tuple
    ]
)

# Tile structure used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over
        ("transparent", np.bool),  # True if this tile doesn't block FOV
        ("dark", graphic_dt)  # Graphics for when this tile is not in FOV
    ]
)


def new_tile(
        *,  # Forces use of keywords
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
):
    """
    Helper function for defining individual types
    :param walkable: int(); Can this tile be walked over?
    :param transparent: int(); Does this tile block FOV?
    :param dark: Tuple[int(), Tuple[int(), int(), int()], Tuple[int(), int(), int()]];
                 How does this character appear when out of FOV?
                 Filled via Tuple[unicode_char, Tuple[foreground_RGB], Tuple[background_RGB]]
    :return:
    """
    return np.array((walkable, transparent, dark), tile_dt)


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (0, 0, 0))
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (255, 255, 255), (0, 0, 0))
)
