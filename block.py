
import pygame as pg
import random
import math

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

class Block:
    def __init__(self, num, pos):
        self.num = num
        self.rect = pg.Rect(
            pos[0],
            pos[1],
            BLOCK_SIDE,
            BLOCK_SIDE
        )

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

    def getMove(self, roff):
        block = Block(self.num, (self.rect.x, self.rect.y))
        block.rect.move_ip(*roff)
        return block

    def checkCollision(self, block):
        return self.num != block.num and self.rect.colliderect(block.rect)

    def checkMerge(self, block):
        center = (block.rect.x + BLOCK_SIDE//2, block.rect.y + BLOCK_SIDE//2)
        return self.num == block.num and self.rect.collidepoint(center)
