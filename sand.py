import random


class Sand:
    type = 1
    color = (253, 238, 115)

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.frame = 0
        self.static = False

    def can_move(self, pixels):
        if self.y + 1 < len(pixels[0]):
            if pixels[self.x][self.y + 1] == 0:
                return True, 0, 1
            if self.frame % 2 == 0:
                if self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1] == 0:
                    return True, 1, 1
                elif self.x - 1 > -1 and pixels[self.x - 1][self.y + 1] == 0:
                    return True, -1, 1
            else:
                if self.x - 1 > -1 and pixels[self.x - 1][self.y + 1] == 0:
                    return True, -1, 1
                elif self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1] == 0:
                    return True, 1, 1
        self.static = True
        return False, 0, 0

    def move(self, pixels, frame):
        movable, x, y = self.can_move(pixels)
        if self.frame == frame:
            return
        if movable:
            for a in range(self.x - 1, self.x + 2):
                for b in range(self.y - 1, self.y + 2):
                    if 0 < a < len(pixels) and 0 < b < len(pixels[0]):
                        if pixels[a][b] != 0:
                            if pixels[a][b].static:
                                pixels[a][b].static = False
            self.x += x
            self.y += y
            self.frame = frame
            pixels[self.x][self.y] = self
            pixels[self.x - x][self.y - y] = 0

    def draw(self, pg, screen):
        pg.draw.rect(screen, Sand.color, (self.x, self.y, 1, 1))
