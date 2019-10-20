import pygame as pg
import random
import math

from copy import deepcopy

NUM_BLOCKS = 21
WIDTH_SIZE = 7
HEIGHT_SIZE = 8
BLOCK_SIDE = 50
BLOCK_DROP_VEL = 10

def genRndBlock(num_lim = NUM_BLOCKS-1):
    if num_lim >= NUM_BLOCKS:
        num_lim = NUM_BLOCKS - 1

    num = random.randint(1, num_lim)
    x = random.randint(0, WIDTH_SIZE-1) * BLOCK_SIDE
    y = random.randint(0, HEIGHT_SIZE-1) * BLOCK_SIDE

    return Block(num, (x, y))

def getSelected(blocks):
    for i, block in enumerate(blocks):
        if block.selected:
            return i
    return -1

def getCollided(blocks, pos):
    for i, block in enumerate(blocks):
        if block.rect.collidepoint(pos):
            return i
    return -1

class Block:
    def __init__(self, num, pos):
        self.num = num
        self.rect = pg.Rect(
            pos[0],
            pos[1],
            BLOCK_SIDE,
            BLOCK_SIDE
        )
        self.selected = False

    def __repr__(self):
        return 'Block({}, {}, {})'.format(self.num, self.rect, self.selected)

    def isValid(self):
        if 0 >= self.num or self.num >= NUM_BLOCKS:
            return False
        if 0 > self.rect.x or self.rect.x >= WIDTH_SIZE * BLOCK_SIDE:
            return False
        if 0 > self.rect.y or self.rect.y >= HEIGHT_SIZE * BLOCK_SIDE:
            return False
        return True

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def getDrop(self):
        block = self.getMove((0, BLOCK_DROP_VEL))
        return block

    def getMove(self, roff=(0, 0)):
        block = deepcopy(self)
        xdir = 1 if roff[0] >= 0 else -1
        ydir = 1 if roff[1] >= 0 else -1
        nroff = (
            BLOCK_DROP_VEL * xdir if abs(roff[0]) > 5 else 0,
            BLOCK_DROP_VEL * ydir if abs(roff[1]) > 5 else 0
        )
        block.rect.move_ip(*nroff)
        return block

    def checkCollision(self, block):
        return self.num != block.num and self.rect.colliderect(block.rect)

    def checkMerge(self, block):
        center = (block.rect.x + BLOCK_SIDE//2, block.rect.y + BLOCK_SIDE//2)
        return self.num == block.num and self.rect.collidepoint(center)