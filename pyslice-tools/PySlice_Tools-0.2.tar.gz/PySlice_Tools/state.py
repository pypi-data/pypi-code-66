""" This module provides a class to keep track of the internal state
of the application.
"""
import os.path
import PySlice_Tools.slice._slice
import json

from PySlice_Tools.cube import Cube


class State:
    def __init__(self, canvas, ax):
        self._canvas = canvas
        self._ax = ax
        self._cube_map = dict()
        self._command_list = []
        self._commanad_index = 0
        self._command_options = ['addcube', 'delcube', 'save', 'load', 'clear','delcubeset', 'addcubeset', 'addmodel', 'submodel', 'help', 'slice'] #Used for tab autocomplete
        self._current_color = (0, .7, 1, .8)    #Default RGBA cube color

    def add_cube(self, pos, color=None):
        # If a cube is already added at the position given,
        # don't do anything
        if pos in self._cube_map:
          print('A cube has already been added at the given position', flush=True)
          return -1

        # If color not passed in, use last set color. Else, set _current_color to passed in color
        if color == None:
            color = self._current_color
        else:
            self._current_color = color

        # resize grid if new cube is out of axis limit
        low = min(pos) - 1
        low = min(low, self._ax.get_xlim()[0])
        high = max(pos) + 1
        high = max(high, self._ax.get_xlim()[1])
        self._ax.set_xlim(low, high, 1)
        self._ax.set_ylim(low, high, 1)
        self._ax.set_zlim(low, high, 1)

        # Draw cube on canvas
        cube = Cube(self._ax, pos, color)
        cube.draw()

        self._canvas.draw()

        # Add cube to internal map
        self._cube_map[pos] = cube

        return 1

    def delete_cube(self, pos):
        """
        Delete a cube given x, y, z position as a tuple.
        Return -1 if cube deletion not successful and 1 if successful.
        """
        if not self.has_cube(pos):
          print('Cube does not exist', flush=True)
          return -1

        # Remove cube from canvas by setting it to transparent
        cube = self._cube_map[pos]
        cube.remove()
        self._canvas.draw()

        # Remove cube from internal map
        del self._cube_map[pos]

        return 1

    def has_cube(self, pos):
        return pos in self._cube_map

    def get_cube_list(self):
        return list(self._cube_map.keys())

    def get_possible_commands(self):
        return self._command_options

    def save_cubes_to_file(self, filename, directory='./'):    # Default directory is cwd if no dir passed in
        with open(os.path.join(directory, filename + '.slice'), 'w+') as f:
            for pos in self.get_cube_list():
                color = self._cube_map[pos].color
                f.write(str(pos[0]) + ' ' + 
                        str(pos[1]) + ' ' + 
                        str(pos[2]) + ' ' + 
                        str(color[0]) + ' ' +   # Cube color tuple in the form (R, G, B, transparency)
                        str(color[1]) + ' ' +
                        str(color[2]) + ' ' +
                        str(color[3]) + '\n')

    def clear(self): # clear clears all of the cubes from the display
        # re-draw canvas
        self._ax.clear()
        self._ax.set_xlim(0, 5, 1)
        self._ax.set_ylim(0, 5, 1)
        self._ax.set_zlim(0, 5, 1)
        self._ax.set_xlabel('X')
        self._ax.set_ylabel('Y')
        self._ax.set_zlabel('Z')
        self._canvas.draw()
        self._cube_map.clear()
        
    def load_cubes_to_file(self, directory,clear=True, offset=(0, 0, 0)): #clear is an optional paramater. Set to true by default.  Offset is optional
        try:
            file = open(directory, "r")
        except: 
             print('File does not exist', flush=True)
             return
        if(clear):
            self.clear()
        for cube in file:
            cube_stats = cube.split(' ')
            pos = (int(cube_stats[0]) + offset[0],int(cube_stats[1]) + offset[1],int(cube_stats[2]) + offset[2])
            r = float(cube_stats[3])
            g = float(cube_stats[4])
            b = float(cube_stats[5])
            a = float(cube_stats[6].rstrip('\n'))
            self.add_cube(pos,(r,g,b,a))

    def delete_cube_set(self,x,y,z,sx,sy,sz):
        for i in range(0, sx):
            for j in range(0, sy):
                for k in range(0, sz):
                    pos = (i + x, j + y, k + z)
                    if(pos in self.get_cube_list()):
                        self.delete_cube(pos) 

    def get_current_color(self):
        return self._current_color

    def save_command(self, command):
        self._command_list.append(command)
        self._commanad_index = len(self._command_list)

    def get_last_command(self):
        if len(self._command_list) == 0:
            return ''
        self._commanad_index -= 1
        if self._commanad_index < 0:
            self._commanad_index = 0
        return self._command_list[self._commanad_index]

    def get_next_command(self):
        self._commanad_index += 1
        if self._commanad_index >= len(self._command_list):
            self._commanad_index = len(self._command_list)
            return ''
        return self._command_list[self._commanad_index]

    def add_design(self, directory, offset):
        self.load_cubes_to_file(directory, False, offset)

    def subtract_design(self, directory, offset):
        try:
            file = open(directory, "r")
        except: 
             print('File does not exist', flush=True)
             return
        for cube in file:
            cube_stats = cube.split(' ')
            pos = (int(cube_stats[0]) + offset[0],int(cube_stats[1]) + offset[1],int(cube_stats[2]) + offset[2])
            self.delete_cube(pos)

    def get_help_description(self, option=''):
        with open("command_help.json") as f:
            data = json.load(f)     #Load help descriptions from .json file as dict

        if option == '':
            return 'Possible commands:\n\n' \
                   + '\n'.join(self.get_possible_commands()) \
                   + '\n\nType help [command] to get more info on specific command.'

        return data['commands'][option]       #Return dict that includes command's description and example (optional)

    def run_cpp(self, directory):
        #assert 'runslice' in dir(slice)
        #assert callable(slice.runslice)
        print(PySliceTools.slice._slice.runslice(directory))


    def add_cube_set(self, x, y, z, sx, sy, sz, color=None):
        for i in range(0, sx):
            for j in range(0, sy):
                for k in range(0, sz):
                    pos = (i + x, j + y, k + z)
                    self.add_cube(pos, color)
