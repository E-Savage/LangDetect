import curses
from menu import Menu
import sys

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

global title

def main(scr):
    running = True

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

    items = ["Language Detection", "Help Page", "About page", "Exit"]

    while running:
        scr.addstr(0,0, title)
        scr.refresh()
        menu = Menu(items, scr, 11, 4)
        result = menu.run()
        win = curses.newwin(9, 86, 16, 4)

        if items[result] == 'Language Detection':
            #here is something
            t = 4
            
        elif items[result] == 'Help Page':
            '''
            if this is selected should display a sub window with the stuff in it 
            '''
            #                   h   w   y   x
            win.clear()
            win.touchwin()
            scr.refresh()
            win.box()
            win.addstr(0, 0, "Help Page") 
            win.addstr(1, 1, "(1) Language detection, option takes user to language detection page  allows user to")
            win.addstr(2, 5, "enter text to determine language of the text, to quit this mode press q and then")
            win.addstr(3, 5, "enter to be taken back to this main screen")
            win.addstr(4, 1, "(2) Help Page, it pulled up this tiny window you are looking at now. It gives you")
            win.addstr(5, 5, "information on how to use the program and what each button does.")
            win.addstr(6, 1, "(3) About Page, this page tells you more about the program and it purpose")
            win.addstr(7, 1, "(4) Exit, quits the program")
            win.refresh()
            scr.refresh()
        elif items[result] == 'About page':
            '''
            if this is selected it should display a subwindow with stuff in it, the stuff is about the about page
            '''
            win.clear()
            win.touchwin()
            scr.refresh()
            win.box()
            win.addstr(0, 0, "About Page")
            win.addstr(1, 1, "This app is a final project for CIS 542 Digital Forensics. Topic chosen was")
            win.addstr(2, 1, "detection of languages from text or audio. I decided to go with text. This")
            win.addstr(3, 1, "project's purpose was to give me a tutorial on how to incorporate ML in to")
            win.addstr(4, 1, "a terminal based application using Python and the curses library. Also,")
            win.addstr(5, 1, "this project allowed me to learn python curses as well. Overall, this")
            win.addstr(6, 1, "project was fun to program and learn from. In the future I would like to")
            win.addstr(7, 1, "add more features and flesh the app out more. Thank you for using my app!")
            win.refresh()
            scr.refresh()
        elif items[result] == 'Exit':
            running = False
        else:
            pass
        scr.refresh()

def menu_print(items, scr):
    curses.curs_set(0)
    menu = Menu(items, scr, 11, 4)
    result = menu.run()
    return result

if __name__ == "__main__":
    curses.wrapper(main)

