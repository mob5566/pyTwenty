#!/usr/bin/env python

import pygame as pg
import sys, os
import random
from os import path

from block import *

# System settings
PROJ_DIR = path.dirname(path.realpath(sys.argv[0]))

# plotting settings
FPS = 60
TITLE_HEIGHT = 30
SCREEN_SIZE = (
    COL_SIZE * BLOCK_SHIFT + GAP_WIDTH,
    ROW_SIZE * BLOCK_SHIFT + GAP_WIDTH
)
QUIT_KEYS = {pg.K_ESCAPE, pg.K_q}

# plotting materials
BLOCK_IMGS = []

# game settings
DURATION = 5

def main():
    global screen, fps
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    fps = pg.time.Clock()
    pg.display.set_caption('Twenty')
    screen.fill((255, 255, 255))

    loadImages()

    while True:
        game_over = False

        for event in pg.event.get():
            if gameQuitEvent(event):
                print('Get quit event')
                game_over = True

            if gameStartEvent(event):
                print('Get start event')
                gameMain()

        pg.display.update()
        fps.tick(FPS)

        if game_over:
            pg.quit()
            break

    return True

def gameMain():
    tw_count = 0
    highest_score = 1
    game_quit = False
    cur_blocks = dict()

    for _ in range(10):
        block = genRndBlock(2)

        if block.pos not in cur_blocks:
            cur_blocks[block.pos] = block

    while True:
        for event in pg.event.get():
            if gameQuitEvent(event):
                print('Get quit event')
                game_quit = True

        drawGame(cur_blocks)

        if game_quit:
            break

        pg.display.update()
        fps.tick(FPS)

    return True

def drawGame(blocks):
    for block in blocks.values():
        screen.blit(BLOCK_IMGS[block.num], (block.rx, block.ry))

def gameStartEvent(event):
    start = False

    if event.type == pg.KEYDOWN:
        start = event.key not in QUIT_KEYS

    return start

def gameQuitEvent(event):
    quit = False

    if event.type == pg.QUIT:
        quit = True
    elif event.type == pg.KEYDOWN:
        quit = event.key in QUIT_KEYS

    return quit

def loadImages():
    global BLOCK_IMGS
    BLOCK_IMGS = [pg.image.load(path.join(PROJ_DIR, 'assets',
    'num_{}.png'.format(num))).convert_alpha() for num in range(NUM_BLOCKS)]

if __name__ == '__main__':
    main()
