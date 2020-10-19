""" This module provides a cube class.
"""

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


class Cube:
    def __init__(self, ax, pos, color):
        self._ax = ax
        self._pos = pos
        self._color = color
        self.faces = None

    @property
    def pos(self):
        return self._pos

    @property
    def color(self):
        return self._color

    def draw(self):
        (x, y, z) = self._pos
        cube_definition = self.generate_cube_def(x, y, z)
        
        # https://stackoverflow.com/questions/44881885/python-draw-parallelepiped
        cube_definition_array = [
            np.array(list(item))
            for item in cube_definition
        ]

        points = []
        points += cube_definition_array
        vectors = [
            cube_definition_array[1] - cube_definition_array[0],
            cube_definition_array[2] - cube_definition_array[0],
            cube_definition_array[3] - cube_definition_array[0]
        ]

        points += [cube_definition_array[0] + vectors[0] + vectors[1]]
        points += [cube_definition_array[0] + vectors[0] + vectors[2]]
        points += [cube_definition_array[0] + vectors[1] + vectors[2]]
        points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

        points = np.array(points)

        edges = [
            [points[0], points[3], points[5], points[1]],
            [points[1], points[5], points[7], points[4]],
            [points[4], points[2], points[6], points[7]],
            [points[2], points[6], points[3], points[0]],
            [points[0], points[2], points[4], points[1]],
            [points[3], points[6], points[7], points[5]]
        ]

        self.faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
        self.faces.set_facecolor(self._color)

        self._ax.add_collection3d(self.faces)

        # Plot the points themselves to force the scaling of the axes
        self._ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=0)

    def remove(self):
        self.faces.set_facecolor((0, 0, 0, 0))
        self.faces.set_edgecolor((0, 0, 0, 0))

    def generate_cube_def(self, x, y, z):
        return [(x, y, z), (x, y + 1, z), (x + 1, y, z), (x, y, z + 1)]
