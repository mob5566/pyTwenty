
import random

NUM_BLOCKS = 21
ROW_SIZE = 8
COL_SIZE = 7
GAP_WIDTH = 1
BLOCK_SIDE = 50
BLOCK_SHIFT = GAP_WIDTH + BLOCK_SIDE

def genRndBlock(num_lim = NUM_BLOCKS-1):
    if num_lim >= NUM_BLOCKS:
        num_lim = NUM_BLOCKS - 1

    num = random.randint(1, num_lim)
    x = random.randint(0, ROW_SIZE-1)
    y = random.randint(0, COL_SIZE-1)

    return Block(num, (x, y))

class Block:
    def __init__(self, num, pos):
        assert 0 <= num and num < NUM_BLOCKS
        assert 0 <= pos[0] and pos[0] < ROW_SIZE
        assert 0 <= pos[1] and pos[1] < COL_SIZE

        self.num = num
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

        self.rx = self.x * BLOCK_SHIFT + GAP_WIDTH
        self.ry = self.y * BLOCK_SHIFT + GAP_WIDTH
