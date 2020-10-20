"""
TODO
"""

import curses
import _curses
import time

from .user_defined import UserDefined
from .widgets.builtin_widgets import TitleBarWidget, StatusBarWidget, BackgroundWidget
from .fmt import FmtString
from . import renderer
from .color import color

version = "0.0.3"


class TUI(UserDefined):
    """
    TODO
    """

    def run(self):
        """TODO"""
        self.__pre_setup()
        self.setup()  # User defined

        while self.__is_running:
            curses.wrapper(self.__error_handling_loop)

        self.cleanup()  # User defined

    def __pre_setup(self):
        """TODO"""
        self.__is_running = True
        self.__cursor_visible = False
        self.__wait = True
        self.__clear = False
        self.__framerate = 5
        self.__framecount = 0
        self.__last_draw_time = time.time()
        self.__key = None
        self.__clear_y1 = None
        self.__clear_x1 = None
        self.__clear_y2 = None
        self.__clear_x2 = None

        self.__title_bar = TitleBarWidget()
        self.__status_bar = StatusBarWidget()
        self.__background = BackgroundWidget()

        self.origin_x = 0
        self.origin_y = 0

    def __error_handling_loop(self, screen):
        """TODO"""
        try:
            self.__execution_loop(screen)
        except _curses.error:
            event = screen.getch()
            if event == curses.KEY_RESIZE:
                self.window_resized()  # User defined
            else:
                raise

    def __execution_loop(self, screen):
        """TODO"""
        curses.curs_set(self.__cursor_visible)
        curses.start_color()
        curses.use_default_colors()
        screen.keypad(True)

        self.screen = screen

        if self.framecount() == 0:
            self.__draw()

        if self.__wait:
            # Wait until the next user input
            self.screen.nodelay(0)
            key = screen.getch()
            self.__key = self.__clean_key(key)

        else:
            """
            Do not wait if no imput given. This means the program
            will continuously run regardless of user input. Stop
            and wait the amount of time defined by the framerate
            """
            self.screen.nodelay(1)
            key = screen.getch()
            if key != -1:
                self.__key = self.__clean_key(key)
            else:
                self.__key = None
            
            time.sleep(1 / self.__framerate)

        if self.__clear:
            self.__clear_screen()

        self.__draw()

        if self.__key:
            self.key_pressed(self.__key)
            self.__key = None

        self.__framecount += 1

    def __draw(self):
        """Draw builtin widgets and run user defined draw() method"""
        self.__draw_builtin_widgets()
        self.draw()  # User defined
        self.screen.refresh()

    def __clear_screen(self):
        """Clear the screen. Only run if user has called self.clear() within
        the current loop iteration"""

        if self.__clear_y1 is not None:
            """
            If self.clear() call with parameters (y1, x1, y2, x2) then clear only
            the portion of the screen defined by those cordinates

            TODO test that this works correctly with the coordinates specified
            """
            for row in range(self.__clear_y1,  self.__clear_y2 + 1):
                self.write(row, self.__clear_x1, ' ' * (self.__clear_x2 - self.__clear_x1))

            # Reset clearing coordinates
            self.__clear_y1 = None
            self.__clear_x1 = None
            self.__clear_y2 = None
            self.__clear_x2 = None

        else:
            # Clear the entire screen
            self.screen.clear()

        # Reset the self.__clear variable
        self.__clear = False

    def __clean_key(self, key):
        return key

    ###########################
    """ User UI controllers """
    ###########################

    def hide_cursor(self):
        """Hid the cursor on screen"""
        self.__cursor_visible = False

    def show_cursor(self):
        """Show the cursor on screen"""
        self.__cursor_visible = True

    def wait_for_input(self):
        """Instruct the execution loop to wait for user input"""
        self.__wait = True

    def no_wait_for_input(self):
        """Instruct the execution loop to not wait for user input"""
        self.__wait = False

    def framerate(self, framerate):
        """Set the framerate
        --------------------
        :param: framerate
            :type: float or int
        """
        self.__framerate = framerate

    def framecount(self):
        return self.__framecount

    def exit(self):
        """Instruct the execution loop to exit the program safely"""
        self.__is_running = False

    def clear(self, y1=None, x1=None, y2=None, x2=None):
        """Instruct the execution loop to clear the screen at the end
        of the current iteration. If paramters given (y1, x1, y2, x2)
        only clear the portions of the screen defined by these given
        coordinates
        -------------------------------------------------------------
        """

        if None in [y1, x1, y2, x2] and any([y1, x1, y2, x2]):
            raise ValueError('Clearing only portions of the screen '
                             'requires all four coordinates you would '
                             'like to clear inside: y1, x1, y2, x2')

        self.__clear = True
        self.__clear_y1 = y1
        self.__clear_x1 = x1
        self.__clear_y2 = y2
        self.__clear_x2 = x2

    def get_width(self):
        """Return the current width of the screen"""
        width = self.screen.getmaxyx()[1]
        return width

    def get_height(self, relative=True):
        """Return the height of the screen
        ----------------------------------
        :param: relative
            :type: bool
            :default: True

            If relative is True, do not include the title bar or status bar
            as part of the 'height' of the screen if they are enabled.

            If relative is False, return the actual total height of the screen.
        """
        height = self.screen.getmaxyx()[0]
        if relative:
            if self.__title_bar.is_enabled():
                height -= 1
            if self.__status_bar.is_enabled():
                height -= 1
        return height

    def write(self, y=None, x=None, text='', fg=-1, bg=-1, style=0, relative=True, wrap=False):
        """Wrapper method for renderer.write that will automatically 
        use self.screen as the object to write on
        ------------------------------------------------------------
        """
        if relative:
            y_pos = self.origin_y + y
            x_pos = self.origin_x + x

        if isinstance(text, FmtString):
            for index, (_text, _color) in enumerate(text):
                if index == 0:
                    renderer.write(self.screen, y=y_pos, x=x_pos, text=_text, colors=_color)
                else:
                    renderer.write(self.screen, text=_text, colors=_color)
        else:
            renderer.write(self.screen, y_pos, x_pos, text, fg, bg, style, wrap)

    #######################
    """ Builtin Widgets """
    #######################

    def __draw_builtin_widgets(self):
        """TODO"""
        self.__background.draw(self.screen)
        self.__title_bar.draw(self.screen)
        self.__status_bar.draw(self.screen)

    def enable_title_bar(self, title:str, fg=-1, bg=-1, style=0, justification:str = "center"):
        """TODO"""
        self.__title_bar.enable()
        self.__title_bar.set_title(title=title, fg=fg, bg=bg, style=style)
        self.__title_bar.set_justification(justification)
        self.origin_y += 1
        return self.__title_bar

    def disable_title_bar(self):
        """TODO"""
        self.__title_bar.disable()
        self.origin_y -= 1
        self.clear()

    def hide_title_bar(self):
        """TODO"""
        self.__title_bar.disable()
        self.origin_y -= 1
        self.clear()

    def show_title_bar(self):
        """TODO"""
        self.__title_bar.enable()
        self.origin_y += 1
        self.clear()

    def toggle_title_bar(self):
        """TODO"""
        if self.__title_bar.is_enabled():
            self.__title_bar.disable()
        else:
            self.__title_bar.enable()
        self.clear()

    def enable_status_bar(self, text:str, fg=-1, bg=-1, style=0, justification="left", pad_char=" "):
        """TODO"""
        self.__status_bar.enable()
        self.__status_bar.set_title(title=text, fg=fg, bg=bg, style=style)
        self.__status_bar.set_justification(justification)
        return self.__status_bar

    def disable_status_bar(self):
        """TODO"""
        self.__status_bar.disable()
        self.clear()

    def show_status_bar(self):
        """TODO"""
        self.__status_bar.enable()
        self.clear()

    def hide_status_bar(self):
        """TODO"""
        self.__status_bar.disable()
        self.clear()

    def toggle_status_bar(self):
        """TODO"""
        if self.__status_bar.is_enabled():
            self.__status_bar.disable()
        else:
            self.__status_bar.enable()
        self.clear()

    def enable_background(self, ch=' ', fg=-1, bg=-1, style=0):
        """TODO"""
        self.__background.enable()
        self.__background.set_colors(fg=fg, bg=bg, style=style)
        self.__background.set_ch(ch)
        return self.__background

    def disable_background(self):
        """TODO"""
        self.__background.disable()
        self.clear()

    def hide_background(self):
        """TODO"""
        self.__background.disable()
        self.clear()

    def show_background(self):
        """TODO"""
        self.__background.enable()
        self.clear()

    def toggle_background(self):
        """TODO"""
        if self.__background.is_enabled():
            self.__background.disable()
        else:
            self.__background.enable()
        self.clear()
