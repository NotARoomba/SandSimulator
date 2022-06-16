from element import *
class Water(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = WATER
    def canMove(self, pixels):
        if self.y + 1 < len(pixels[0]):
            if pixels[self.x][self.y + 1].type == VOID:
                return True, 0, 1
            if self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1].type == VOID:
                return True, 1, 1
            elif self.x - 1 > -1 and pixels[self.x - 1][self.y + 1].type == VOID:
                return True, -1, 1
            elif self.x + 1 < len(pixels) and pixels[self.x + 1][self.y].type == VOID:
                return True, 1, 0
            elif self.x - 1 > -1 and pixels[self.x - 1][self.y].type == VOID:
                return True, -1, 0
        return False, 0, 0

