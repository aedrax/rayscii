#!/usr/bin/python3

import curses
from time import sleep


def main():
    # determine the terminal type, send any required setup codes to the
    # terminal, and create various internal data structures
    stdscr = init_curses_window()

    stdscr.addstr(0, 0, "Test", curses.A_REVERSE)
    stdscr.refresh()
    # wait 2 seconds before cleaning up curses
    sleep(2)

    end_curses_window(stdscr)

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
