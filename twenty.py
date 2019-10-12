#!/usr/bin/env python

import pygame as pg
import numpy as np
import sys

MATRIX_SIZE = (7, 8)
TITLE_HEIGHT = 30
BLOCK_SIDE = 50
GAP_WIDTH = 5
SCREEN_SIZE = (
    MATRIX_SIZE[0]*(BLOCK_SIDE+GAP_WIDTH) + GAP_WIDTH,
    MATRIX_SIZE[1]*(BLOCK_SIDE+GAP_WIDTH) + GAP_WIDTH
)
QUIT_KEYS = {pg.K_ESCAPE, pg.K_q}

def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption('Twenty')

    while True:
        game_over = False

        for event in pg.event.get():
            if game_quit_event(event):
                game_over = True

            if game_start_event(event):
                game_main()

        if game_over:
            pg.quit()
            break

    return True

def game_main():
    pass

def game_start_event(event):
    start = False

    if event.type == pg.KEYDOWN:
        start = event.key not in QUIT_KEYS

    return start

def game_quit_event(event):
    quit = False

    if event.type == pg.QUIT:
        quit = True
    elif event.type == pg.KEYDOWN:
        quit = event.key in QUIT_KEYS

    return quit

if __name__ == '__main__':
    main()
