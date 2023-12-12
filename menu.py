import curses

class Menu:
    def __init__(self, items, stdscr, sx, sy):
        self.items = items
        self.selected_item = 0
        self.stdscr = stdscr
        self.x = sx
        self.y = sy

    def display(self):
        # self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        for i, item in enumerate(self.items):
            x = self.x + i
            y = self.y
            if i == self.selected_item:
                self.stdscr.attron(curses.A_REVERSE)
                self.stdscr.addstr(x, y, item)
                self.stdscr.attroff(curses.A_REVERSE)
            else:
                self.stdscr.addstr(x, y, item)
        self.stdscr.refresh()

    def run(self):
        while True:
            self.display()
            key = self.stdscr.getch()
            if key == curses.KEY_UP and self.selected_item > 0:
                self.selected_item -= 1
            elif key == curses.KEY_DOWN and self.selected_item < len(self.items) - 1:
                self.selected_item += 1
            elif key == 10:  # Enter key
                return self.selected_item


#this was a test to see how the menu would print

# def main(stdscr):
#     curses.curs_set(0)
#     items = ["Language Detection", "Help Page", "About page", "Exit"]
#     menu = Menu(items, stdscr)
#     result = menu.run()
#     stdscr.clear()
#     stdscr.addstr(0, 0, f"You selected: {items[result]}")
#     stdscr.refresh()
#     stdscr.getch()


# if __name__ == "__main__":
#     curses.wrapper(main)
