#!/usr/bin/python3

import curses
from time import sleep


def main():
    try:
        # determine the terminal type, send any required setup codes to the
        # terminal, and create various internal data structures
        stdscr = init_curses_window()
        run(stdscr)
    finally:
        end_curses_window(stdscr)
    
        

def run(stdscr):
    stdscr.refresh()
    # wait 2 seconds before cleaning up curses
    sleep(2)

    x = 0
    y = 0
    while True:
        stdscr.addstr(y, x, "X", curses.A_REVERSE)
        c = stdscr.getch()
        if c == ord('w'):
            y -= 1
        elif c == ord('a'):
            x -= 1
        elif c == ord('s'):
            y += 1
        elif c == ord('d'):
            x += 1
        x, y = check_bounds(stdscr, x, y)

def check_bounds(window, x, y):
    y_max, x_max = window.getmaxyx()
    x_max -= 1
    y_max -= 1
    
    if x < 0:
        x = 0
    elif x > x_max:
        x = x_max
    if y < 0:
        y = 0
    elif y > y_max:
        y = y_max
    return x, y

def end_curses_window(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    # restore the terminal to original operating mode
    curses.endwin()

def init_curses_window():
    # determine the terminal type, send any required setup codes to the
    # terminal, and create various internal data structures
    stdscr = curses.initscr()
    # turn off automatic echoing of keys to the screen
    curses.noecho()
    # eact to keys instantly, without requiring the Enter key to be pressed
    curses.cbreak()
    # enable keypad mode
    stdscr.keypad(True)
    # make curson invisible
    curses.curs_set(False)

    # clear screen
    stdscr.clear()
    return stdscr

if __name__ == "__main__":
    main()
