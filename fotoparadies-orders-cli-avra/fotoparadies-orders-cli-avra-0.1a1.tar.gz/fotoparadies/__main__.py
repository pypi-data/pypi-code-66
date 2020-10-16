import curses
from curses import panel
from . import api
import argparse


parser = argparse.ArgumentParser(description='Check your photo orders from fotoparadies.')
parser.add_argument('--shop', '-s', help='shop number, used for direct api call')
parser.add_argument('--order', '-o', help='order number, used for direct api call')
parser.add_argument('--json', help='return json of api call if using --shop and --order', action='store_true')

args = parser.parse_args()

if args:
    if args.order and args.shop:
        order_info = api.get_order_info(args.shop, args.order)
        if args.json:
            print(order_info)
        else:
            print(f'{order_info["summaryDate"]}: {order_info["summaryStateCode"]}')
            print(f'{order_info["summaryStateText"]}')
            print(f'Total of {order_info["summaryPriceText"]}'.replace(u'\xa0', u' '))
        exit()

class Menu(object):
    def __init__(self, items, stdscr):
        self.window = stdscr.subwin(3,3)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.items = items
        self.current_entry = 0

    def navigate(self, direction):
        self.current_entry += direction
        if self.current_entry < 0:
            self.current_entry = len(self.items) - 1
        elif self.current_entry >= len(self.items):
            self.current_entry = 0

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.current_entry:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = f'{index + 1}  {item[0]}'
                self.window.addstr(index + 1, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.current_entry == len(self.items) - 1:
                    break
                else:
                    self.items[self.current_entry][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)
            elif key == ord('q'):
                break 
    
    

def new_order():
    pass


def main(stdscr):

    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(2, 4, 'fotoparadies orders cli')

    orders_menu_entries = [
        ('test', 0),
        ('back', 0)
    ]
    orders_menu = Menu(orders_menu_entries, stdscr)

    home_menu_entries = [
        ('see orders', orders_menu.display),
        ('check/add new order', new_order),
        ('exit',0)
    ]
    home_menu = Menu(home_menu_entries, stdscr)


    home_menu.display() 

    stdscr.refresh()
    # stdscr.getkey()


curses.wrapper(main)

