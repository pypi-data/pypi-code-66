"""Provides the Menu class."""

from pathlib import Path
from time import time
from typing import Callable, List, Optional

from attr import Factory, attrib, attrs
from pyglet.window import key

from ..action import ActionFunctionType, OptionalGenerator
from ..hat_directions import DOWN, LEFT, RIGHT, UP
from ..level import Level
from ..mixins import DismissibleMixin, TitleMixin
from .menu_item import MenuItem


@attrs(auto_attribs=True)
class Menu(Level, TitleMixin, DismissibleMixin):
    """A menu which holds multiple menu items which can be activated using
    actions.

    As menus are simply :class:`~earwax.level.Level` subclasses, they can be
    :meth:`pushed <earwax.game.Game.push_level>`, :meth:`popped
    <earwax.game.Game.pop_level>`, and :meth:`replaced
    <earwax.game.Game.replace_level>`.

    To add items to a menu, you can either use the :meth:`item` decorator, or
    the :meth:`add_item` function.

    Here is an example of both methods::

        from earwax import Game, Level, Menu, tts
        from pyglet.window import key, Window
        w = Window(caption='Test Game')
        g = Game()
        l = Level()
        @l.action('Show menu', symbol=key.M)
        def menu():
            '''Show a menu with 2 items.'''
            m = Menu('Menu', g)
            @m.item('First Item')
            def first_item():
                tts.speak('First menu item.')
                g.pop_level()
            def second_item():
                tts.speak('Second menu item.')
                g.pop_level()
            m.add_item('Second Item', second_item)
            g.push_level(m)

        g.push_level(l)
        g.run(w)

    To override the default actions that are added to a menu, subclass
    :class:`earwax.Menu`, and override :meth:`__attrs_post_init__`.

    :ivar ~earwax.Menu.item_sound_path: The default sound to play when moving
        through the menu.

        If the selected item's :attr:`~earwax.MenuItem.sound_path` attribute is
        not ``None``, then that value takes precedence.

    :ivar ~earwax.Menu.items: The list of MenuItem instances for this menu.

    :ivar ~earwax.Menu.position: The user's position in this menu.

    :ivar ~earwax.Menu.search_timeout: The maximum time between menu searches.

    :ivar ~earwax.Menu.search_time: The time the last menu search was
        performed.

    :ivar ~earwax.Menu.search_string: The current menu search search string.
    """

    item_select_sound_path: Optional[Path] = None
    item_activate_sound_path: Optional[Path] = None

    position: int = -1
    search_timeout: float = 0.5
    search_time: float = 0.0

    search_string: str = attrib(default=Factory(str), init=False)
    items: List[MenuItem] = attrib(default=Factory(list), init=False)

    def __attrs_post_init__(self) -> None:
        """Initialise the menu."""
        self.action('Activate item', symbol=key.RETURN, hat_direction=RIGHT)(
            self.activate
        )
        self.action('Dismiss', symbol=key.ESCAPE, hat_direction=LEFT)(
            self.dismiss
        )
        self.action('Move down', symbol=key.DOWN, hat_direction=DOWN)(
            self.move_down
        )
        self.action('Move up', symbol=key.UP, hat_direction=UP)(
            self.move_up
        )
        self.motion(key.MOTION_BEGINNING_OF_LINE)(self.home)
        self.motion(key.MOTION_END_OF_LINE)(self.end)
        self.register_event_type(self.on_text.__name__)
        super().__attrs_post_init__()

    @property
    def current_item(self) -> Optional[MenuItem]:
        """Return the currently selected menu item. If position is -1, return
        ``None``."""
        if self.position != -1:
            return self.items[self.position]
        return None

    def item(self, title: str, **kwargs) -> Callable[
        [ActionFunctionType], MenuItem
    ]:
        """Decorate a function to be used as a menu item.

        For example::

            @menu.item('Title')
            def func():
                pass

            @menu.item('Item with sound', sound_path=Path('sound.wav'))
            def item_with_sound():
                pass

        If you don't want to use a decorator, you can use the
        :meth:`~earwax.Menu.add_item` method instead.

        :param title: The title of the newly created menu item.

        :param kwargs: Extra arguments to be passed to the constructor of
            :class:`earwax.MenuItem`.
        """

        def inner(func: ActionFunctionType) -> MenuItem:
            """Actually add the function."""
            return self.add_item(title, func, **kwargs)

        return inner

    def add_item(
        self, title: str, func: 'ActionFunctionType', **kwargs
    ) -> MenuItem:
        """Add an item to this menu.

        For example::

            m = Menu('Example Menu')
            def f():
                tts.speak('Menu item activated.')
            m.add_item('Test Item', f)
            m.add_item('Item with sound', f, sound_path=Path('sound.wav'))

        If you would rather use decorators, use the :meth:`~earwax.Menu.item`
        method instead.

        :param title: The title of the newly created menu item.

        :param func: The function which will be called when the menu item is
            selected.

        :param kwargs: Extra arguments to be passed to the constructor of
            :class:`earwax.MenuItem`.
        """
        menu_item: MenuItem = MenuItem(title, func, **kwargs)
        self.items.append(menu_item)
        return menu_item

    def show_selection(self) -> None:
        """Speak the menu item at the current position, or :attr:`self.title
        <earwax.level.TitleMixin.title>`, if :attr:`self.position
        <earwax.Menu.position>` is -1.

        This function performs no error checking, so it will happily throw
        errors if :attr:`position` is something stupid."""
        item: Optional[MenuItem] = self.current_item
        if item is None:
            self.game.output(self.title)
        else:
            self.game.output(item.title)
            item.dispatch_event('on_selected')
            sound_path: Optional[Path] = item.select_sound_path or \
                self.item_select_sound_path or \
                self.game.config.menus.default_item_select_sound.value
            if sound_path is not None and \
               self.game.interface_sound_player is not None:
                self.game.interface_sound_player.play_path(sound_path)

    def move_up(self) -> None:
        """Move up in this menu.

        Usually triggered by the up arrow key."""
        self.position = max(-1, self.position - 1)
        self.show_selection()

    def move_down(self) -> None:
        """Move down in this menu.

        Usually triggered by the down arrow key."""
        self.position = min(len(self.items) - 1, self.position + 1)
        self.show_selection()

    def activate(self) -> OptionalGenerator:
        """Activate the currently focused menu item.

        Usually triggered by the enter key."""
        item: Optional[MenuItem] = self.current_item
        if item is not None:
            sound_path: Optional[Path] = item.activate_sound_path or \
                self.item_activate_sound_path or \
                self.game.config.menus.default_item_activate_sound.value
            if sound_path is not None and \
               self.game.interface_sound_player is not None:
                self.game.interface_sound_player.play_path(sound_path)
            return item.func()
        return None

    def home(self) -> None:
        """Move to the start of a menu.

        Usually triggered by the home key."""
        self.position = 0
        self.show_selection()

    def end(self) -> None:
        """Move to the end of a menu.

        Usually triggered by the end key."""
        self.position = len(self.items) - 1
        self.show_selection()

    def on_text(self, text: str) -> None:
        """Handle sent text.

        By default, performs a search of this menu.

        :param text: The text that has been sent.
        """
        now: float = time()
        if (now - self.search_time) > self.search_timeout:
            self.search_string = text.lower()
        else:
            self.search_string += text.lower()
        self.search_time = now
        index: int
        item: MenuItem
        for index, item in enumerate(self.items):
            if item.title.lower().startswith(self.search_string):
                self.position = index
                self.show_selection()
                break

    def on_push(self) -> None:
        """This object has been pushed onto a :class:`~earwax.game.Game` instance.

        By default, show the current selection. That will be the same as
        speaking the title, unless :attr:`self.position <earwax.Menu.position>`
        has been set to anything other than -1.."""
        self.show_selection()
