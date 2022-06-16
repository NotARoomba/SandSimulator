import random
from element import Element, VOID, WATER, bresenham


class Water(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = WATER
        self.spread = 5
        self.density = 0

    def can_move(self, pixels):
        if self.y + 1 < len(pixels[0]):
            if pixels[self.x][self.y + 1].type == VOID:
                return True, 0, 1
            if self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1].type == VOID:
                return True, 1, 1
            elif self.x - 1 > -1 and pixels[self.x - 1][self.y + 1].type == VOID:
                return True, -1, 1
        if random.getrandbits(1):
            for i in reversed(list(bresenham(self.x, self.y, self.x + self.spread, self.y))):
                if 0 > i[0] or i[0] >= len(pixels) or 0 > i[1] or i[1] >= len(pixels[0]):
                    continue
                if pixels[i[0]][i[1]].type == VOID:
                    return True, i[0] - self.x, i[1] - self.y
        for i in reversed(list(bresenham(self.x, self.y, self.x - self.spread, self.y))):
            if 0 > i[0] or i[0] >= len(pixels) or 0 > i[1] or i[1] >= len(pixels[0]):
                continue
            if pixels[i[0]][i[1]].type == VOID:
                return True, i[0] - self.x, i[1] - self.y
        # if self.x + 1 < len(pixels) and pixels[self.x + 1][self.y].type == VOID:
        #     return True, 1, 0
        # elif self.x - 1 > -1 and pixels[self.x - 1][self.y].type == VOID:
        #     return True, -1, 0
        return False, 0, 0
