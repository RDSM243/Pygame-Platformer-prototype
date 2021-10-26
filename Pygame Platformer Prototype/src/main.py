import os, sys, globals
import pygame as pg
from app import App

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(globals.CAPTION)
    if not globals.RUNFULLSCREEN:
        pg.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
    else:
        pg.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT), pg.FULLSCREEN)
    App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()