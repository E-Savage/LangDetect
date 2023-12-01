import curses
from menu import Menu
import sys

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

global title

# curses.title("Language Detective")


def main(scr):
    curses.echo()

    start_here = 11

    running = True

    #mw = curses.newwin(0, 0)

    # scr.addstr(title)
    # scr.refresh()
    # scr.getch()

    # row, cols = scr.getmaxyx()

    
    # main_win.box()
    # scr.keypad(True)
    # scr.refresh()

    # scr.addstr(start_here, 0, "This is a test line")

    # scr.getch()
    #curses.napms(2000)
    #print_title(scr)
    #scr.refresh()


    title = """
    (                                             (                                       
     )\ )                                          )\ )          )           )             
    (()/(    )       (  (    (     ) (  (    (    (()/(    (  ( /(  (     ( /((   )     (  
     /(_))( /(  (    )\))(  ))\ ( /( )\))(  ))\    /(_))  ))\ )\())))\ (  )\())\ /((   ))\ 
    _))  )(_)) )\ )((_))\ /((_))(_)|(_))\ /((_)  (_))_  /((_|_))//((_))\(_))((_|_))\ /((_)
    | |  ((_)_ _(_/( (()(_|_))(((_)_ (()(_|_))     |   \(_)) | |_(_)) ((_) |_ (_))((_|_))  
    | |__/ _` | ' \)) _` || || / _` / _` |/ -_)    | |) / -_)|  _/ -_) _||  _|| \ V // -_) 
    |____\__,_|_||_|\__, | \_,_\__,_\__, |\___|    |___/\___| \__\___\__| \__||_|\_/ \___| 
                    |___/           |___/                                                  
    """

    scr.addstr(0, 0, title)
    # scr.addstr(11, 4, "teehee") start menu items here  
    # scr.addstr(1, 4, "@") this is where you need to start at for everything else    
    scr.refresh()
    items = ["Language Detection", "Help Page", "About page", "Exit"]

    while running:
        menu = Menu(items, scr, 11, 4)
        result = menu.run()

        if items[result] == 'Language Detection':
            scr.addstr(1, 1, f"{items[result]}")
            scr.refresh()
            '''
            if this is selected it should go into the main app which is language detection
            '''
        elif items[result] == 'Help Page':
            scr.addstr(1, 1, f'{items[result]}')
            scr.refresh()
            '''
            if this is selected should display a sub window with the stuff in it 
            '''
        elif items[result] == 'About page':
            scr.addstr(1, 1, f'{items[result]}')
            scr.refresh()
            '''
            if this is selected it should display a subwindow with stuff in it, the stuff is about the about page
            '''
        elif items[result] == 'Exit':
            running = False
        else:
            pass
        scr.refresh()

# def print_title(scr):
#     title = """
#      (                                             (                                       
#      )\ )                                          )\ )          )           )             
#     (()/(    )       (  (    (     ) (  (    (    (()/(    (  ( /(  (     ( /((   )     (  
#      /(_))( /(  (    )\))(  ))\ ( /( )\))(  ))\    /(_))  ))\ )\())))\ (  )\())\ /((   ))\ 
#     _))  )(_)) )\ )((_))\ /((_))(_)|(_))\ /((_)  (_))_  /((_|_))//((_))\(_))((_|_))\ /((_)
#     | |  ((_)_ _(_/( (()(_|_))(((_)_ (()(_|_))     |   \(_)) | |_(_)) ((_) |_ (_))((_|_))  
#     | |__/ _` | ' \)) _` || || / _` / _` |/ -_)    | |) / -_)|  _/ -_) _||  _|| \ V // -_) 
#     |____\__,_|_||_|\__, | \_,_\__,_\__, |\___|    |___/\___| \__\___\__| \__||_|\_/ \___| 
#                     |___/           |___/                                                  
#     """

#     rows = title.strip().splitlines()

#     title_list = [list(row) for row in rows]

#     for i, row in enumerate(title_list):
#         for j, char in enumerate(row):
#             scr.addstr(i, j, char)

#     scr.refresh()

def menu_print(items, scr):
    curses.curs_set(0)
    menu = Menu(items, scr, 11, 4)
    result = menu.run()
    return result

if __name__ == "__main__":
    curses.wrapper(main)
