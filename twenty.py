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
GAME_SIZE = (
    WIDTH_SIZE * BLOCK_SIDE,
    HEIGHT_SIZE * BLOCK_SIDE
)
SCREEN_SIZE = (
    GAME_SIZE[0],
    GAME_SIZE[1] + TITLE_HEIGHT
)
QUIT_KEYS = {pg.K_ESCAPE, pg.K_q}

# plotting materials
BLOCK_IMGS = []

# game settings
DURATION = 5

def main():
    global screen, fps, game_board
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    game_board = pg.Surface(GAME_SIZE)
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
    cur_blocks = [Block(0, (wid * BLOCK_SIDE, HEIGHT_SIZE * BLOCK_SIDE))
            for wid in range(WIDTH_SIZE)]
    init_check = set()

    for _ in range(10):
        block = genRndBlock(2)

        if block.getPos() not in init_check:
            cur_blocks.append(block)
            init_check.add(block.getPos())

    while True:
        for event in pg.event.get():
            if gameQuitEvent(event):
                print('Get quit event')
                game_quit = True

        cur_blocks = updateGame(cur_blocks)
        drawGame(cur_blocks)

        screen.blit(game_board, (0, TITLE_HEIGHT))

        if game_quit:
            break

        pg.display.update()
        fps.tick(FPS)

    return True

def updateGame(blocks):
    blocks.sort(key=lambda block: block.rect.y, reverse=True)
    ret_blocks = [block for block in blocks if not block.isValid()]
    exists = [True] * len(blocks)

    # drop and check collision
    for i, block in enumerate(blocks):
        if not block.isValid():
            continue

        drop_block = block.getDrop()
        collided = False
        merged = -1

        for j, nxt_block in enumerate(blocks):
            if not exists[j] or i == j:
                continue

            if drop_block.checkCollision(nxt_block):
                collided = True
                break
            elif drop_block.checkMerge(nxt_block):
                merged = j
                break

        if collided:
            ret_blocks.append(block)
        elif merged >= 0:
            blocks[merged].num += 1
            exists[i] = False
        else:
            ret_blocks.append(drop_block)

    return ret_blocks

def drawGame(blocks):
    game_board.fill((255, 255, 255))

    for block in blocks:
        if block.num >= NUM_BLOCKS:
            continue

        game_board.blit(BLOCK_IMGS[block.num], block.rect)

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
