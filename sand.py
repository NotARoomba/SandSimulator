import random
from element import Element, SAND, VOID


class Sand(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = SAND
        self.density = 1

    def can_move(self, pixels):
        if self.y + 1 < len(pixels[0]):
            if pixels[self.x][self.y + 1].type == VOID:
                return True, 0, 1
            right = self.x + 1 < len(pixels) and (pixels[self.x + 1][self.y + 1].type == VOID or pixels[self.x + 1][self.y + 1].density < self.density)
            left = self.x - 1 > -1 and (pixels[self.x - 1][self.y + 1].type == VOID or pixels[self.x - 1][self.y + 1].density < self.density)
            if right and left:
                if random.getrandbits(1):
                    return True, 1, 1
                else:
                    return True, -1, 1
            if right:
                return True, 1, 1
            elif left:
                return True, -1, 1
        return False, 0, 0
