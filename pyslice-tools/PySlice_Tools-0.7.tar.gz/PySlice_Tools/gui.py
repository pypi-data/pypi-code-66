""" This module provides control of application GUI.
"""

from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)
from matplotlib.figure import Figure
import wx
from os import listdir, path

from PySlice_Tools.state import State


class PlotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create 3d plot canvas
        fig = Figure((10, 10), 80)
        self._canvas = FigureCanvas(self, -1, fig)
        self._ax = self.set_ax(fig)

        # Create other widgets
        self._toolbar = self.make_toolbar()
        self._text_ctrl = self.make_textctrl()
        self._color_picker = wx.ColourPickerCtrl(self, colour=(0, 178, 255), style=wx.CLRP_SHOW_ALPHA, size=(80, 30))

        # Add color picker and its label into a sizer
        input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        input_sizer.Add(self._text_ctrl, 1, wx.EXPAND)
        input_sizer.Add(self._color_picker, 0, wx.RIGHT)

        # Put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._canvas, 1, wx.EXPAND | wx.GROW | wx.TOP, border=-50)
        sizer.Add(self._toolbar, 0, wx.GROW)
        sizer.Add(input_sizer, 0, wx.EXPAND)

        # Initialize internal state
        self._state = State(self._canvas, self._ax)

        self.SetSizer(sizer)
        self.Fit()

    def set_ax(self, fig):
        ax = fig.gca(projection='3d')
        ax.set_box_aspect([1, 1, 1])
        ax.set_xlim(0, 5, 1)
        ax.set_ylim(0, 5, 1)
        ax.set_zlim(0, 5, 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

        return ax

    def make_toolbar(self):
        toolbar = NavigationToolbar(self._canvas)
        # Remove the toolbar buttons that we don't need
        for i in range(5):
            toolbar.DeleteToolByPos(3)
        toolbar.Realize()

        return toolbar

    def make_textctrl(self):
        text_ctrl = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER, size=(100, 30))
        text_ctrl.SetFocus()
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        text_ctrl.SetFont(font)
        text_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.execute_command)

        return text_ctrl

    def make_label(self):
        label = wx.StaticText(self, style=wx.ST_ELLIPSIZE_END)
        font = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL)
        label.SetForegroundColour((255, 0, 0))
        label.SetFont(font)

        return label

    def execute_command(self, event):
        # Get command line input value
        input = self._text_ctrl.GetValue()

        # If input is empty, do nothing.
        if not input:
            return

        tokens = input.split()
        self._text_ctrl.SetValue('')
        command = tokens[0]
        size = len(tokens)
        self._state.save_command(input)

        rbg_color = self._color_picker.GetColour()
        # Matplotlib takes in normalized RBG values.
        norm_color = tuple(value / 255 for value in rbg_color)

        if command == 'addcube':
            if size < 4:
                self.display_msg('Error', 'addcube requires x, y, z args.')
                return
            try:
                pos = (int(tokens[1]), int(tokens[2]), int(tokens[3]))
            except ValueError:
                self.display_msg('Error', 'x, y, z are required to be of type integer.')
                return

            res = self._state.add_cube(pos, norm_color)

            if res == -1:
                self.display_msg('Warning', 'A cube has already been added at ' + str(pos))

            print(self._state.get_cube_list(), flush=True)
        elif command == 'delcube':
            if size < 4:
                self.display_msg('Error', 'delcube requires x, y, z args.')
                return

            try:
                pos = (int(tokens[1]), int(tokens[2]), int(tokens[3]))
            except ValueError:
                self.display_msg('Error', 'x, y, z are required to be of type integer.')
                return

            res = self._state.delete_cube(pos)
            if res == -1:
                self.display_msg('Warning', 'Cube not found at ' + str(pos))

            print(self._state.get_cube_list(), flush=True)
        elif command == 'save':
            if size == 1:
                self.display_msg('Error', 'save requires a filename to be specified and optionally a directory.')
                return

            if size == 3:    #If a filename and directory is passed in
                self._state.save_cubes_to_file(tokens[1], tokens[2])
            elif size == 2:                   #If only a filename is passed in
                self._state.save_cubes_to_file(tokens[1])

        elif command == 'clear':
            self._state.clear()
            print("Cubes cleared")
        elif command == 'load':
            if size == 1:
                self.display_msg('Error', 'load requires a file path')
                return
            if size == 2:
                self._state.load_cubes_to_file(tokens[1])
        elif tokens[0] == 'delcubeset':
            if len(tokens) == 7:
                self._state.delete_cube_set(int(tokens[1]),int(tokens[2]),int(tokens[3]),int(tokens[4]),int(tokens[5]),int(tokens[6]))
        elif tokens[0] == 'addmodel':
            if len(tokens) == 2:
                self._state.add_design(tokens[1], (0, 0, 0))
            else:
                self._state.add_design(tokens[1], (int(tokens[2]), int(tokens[3]), int(tokens[4])))
        elif tokens[0] == 'submodel':
            if len(tokens) == 2:
                self._state.subtract_design(tokens[1], (0, 0, 0))
            else:
                self._state.subtract_design(tokens[1], (int(tokens[2]), int(tokens[3]), int(tokens[4])))
        elif tokens[0] == 'help':
            if len(tokens) == 1:
                self.display_msg('Help', self._state.get_help_description())
            elif tokens[1] not in self._state.get_possible_commands():
                 self.display_msg('Error', 'Invalid help argument. For a list of commands, type \'help\'.')
            else:
                help_dict = self._state.get_help_description(tokens[1])
                if 'example' in help_dict:
                    self.display_msg('Help', '\n'.join(["Command: " + tokens[1], '\n', "Description: " + 
                                    help_dict['desc'], '\n', "Example: " + help_dict['example']]))
                else:
                    self.display_msg('Help', '\n'.join(["Command: " + tokens[1], '\n', "Description: " + 
                                    help_dict['desc'],]))
        elif tokens[0] == 'slice':
            self._state.run_cpp(tokens[1])
        elif command == 'addcubeset':
            if size < 7:
                self.display_msg('Error', 'addcubeset requries x, y, z, sx, sy, sz args.')
                return

            try:
                self._state.add_cube_set(int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4]), int(tokens[5]),
                                         int(tokens[6]), norm_color)
            except ValueError:
                self.display_msg('Error', 'arguments are required to be of type integer.')
        elif command == 'delcubeset':
            if size != 7:
                self.display_msg('Error', 'delcubeset requries x, y, z, sx, sy, sz args.')
                return

            try:
                self._state.delete_cube_set(int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4]),
                                            int(tokens[5]), int(tokens[6]))
            except ValueError:
                self.display_msg('Error', 'arguments are required to be of type integer.')
        else:
            self.display_msg('Error', 'Command not found.')

    def display_msg(self, title, content):
        wx.MessageBox(content, title, wx.OK | wx.ICON_INFORMATION)

    def on_key_down(self, event):
        key_pressed = event.GetKeyCode()

        input = self._text_ctrl.GetValue()
        tokens = input.split()
        if key_pressed == wx.WXK_TAB:
            if(len(tokens)>0):
                if(tokens[0] == 'save' or tokens[0] == 'load'or tokens[0] == 'addmodel'or tokens[0] == 'submodel' or tokens[0] == 'slice'):
                    self.tab_complete_file() 
                else:
                    self.tab_complete()
        elif key_pressed == wx.WXK_UP:
            self.show_last_command()
        elif key_pressed == wx.WXK_DOWN:
              self.show_next_command()
        else:
            event.Skip()
            return

    def tab_complete(self):
        current_text = self._text_ctrl.GetValue()
        options  = [cmd for cmd in self._state.get_possible_commands() if cmd.startswith(current_text)] #Grab possible commands based on current text input
        common_prefix = self.longestCommonPrefix(options)
        if common_prefix != '':
            self._text_ctrl.ChangeValue(common_prefix) #Set text to only possible command
            self._text_ctrl.SetInsertionPointEnd()  #Set cursor to EOL

    def tab_complete_file(self):
        filedir = self._text_ctrl.GetValue()
        tokens = filedir.split()
        if(len(tokens) == 2):
            text = tokens[1]
        elif(len(tokens) == 3 and tokens[0]=='save'):
            text = tokens[2]
        elif(len(tokens) > 2):
            return
        else:
            text = ''
        
        path_list = text.split('/')
        current_text = path_list.pop(len(path_list)-1)
        #print('Current Text: ' + current_text)
        #print(path_list)
        filepath = ""
        for p in path_list:
            filepath += p + '/'

        if(filepath == ""):
            test = listdir()
        else:
            try:
                test = listdir(filepath)
            except:
                print("No file path")
                return
        #print(test)
        options  = [file for file in test if file.startswith(current_text)] #Grab possible commands based on current text input
        common_prefix = self.longestCommonPrefix(options)
        if common_prefix != '':
            if(path.isdir(filepath + common_prefix)):
                common_prefix += "/"
            if(len(tokens) == 3 and tokens[0]=='save'):
                self._text_ctrl.ChangeValue(tokens[0]+ ' '+ tokens[1] + ' ' + filepath + common_prefix)
            else:
                self._text_ctrl.ChangeValue(tokens[0] + ' ' + filepath + common_prefix) #Set text to only possible command
            self._text_ctrl.SetInsertionPointEnd()  #Set cursor to EOL


    def show_last_command(self):
        last_command = self._state.get_last_command()
        if last_command:
            self._text_ctrl.SetValue(last_command)
            self._text_ctrl.SetInsertionPointEnd()

    def show_next_command(self):
        next_command = self._state.get_next_command()
        self._text_ctrl.SetValue(next_command)
        self._text_ctrl.SetInsertionPointEnd()

    def longestCommonPrefix(self, str_list):
        #From https://www.studytonight.com/post/finding-longest-common-prefix-in-a-list-of-strings-in-python
        if str_list == []:
            return ''
        if len(str_list) == 1:
            return str_list[0]
        str_list.sort()
        shortest = str_list[0]
        prefix = ''
        for i in range(len(shortest)):
            if str_list[len(str_list) - 1][i] == shortest[i]:
                prefix += str_list[len(str_list) - 1][i]
            else:
                break
        return prefix


# class MyDialog(wx.Dialog):
#    def __init__(self, parent, title):
#       super(MyDialog, self).__init__(parent, title = title, size = (250,150))
#       panel = wx.Panel(self)
#       self.btn = wx.Button(panel, wx.ID_OK, label = "ok", size = (50,20), pos = (75,50))

# class WindowPopup(wx.PopupWindow):
#     def __init__(self, parent, content):
#         wx.PopupWindow.__init__(self, parent)
#
#         # self.SetSize((700, 287))
#         panel = wx.Panel(self)
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         text = wx.StaticText(self, label=content)
#         sizer.Add(text, 0, wx.EXPAND)
#         # st = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.TE_READONLY)
#         # st.SetValue(content)
#         # sizer.Add(st, 0, wx.EXPAND)
#         panel.SetSizer(sizer)


class AppFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='PySlice', pos=(0, 0), size=(800, 850))
        self._plotpanel = PlotPanel(self)
