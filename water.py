import random
class water:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 2
        self.color = (0,0,255)
        self.frame = 0
        self.static = False
        return None
    def canMove(self, pixels):
        #water has a farther movement range than sand
        if self.y + 1 < len(pixels[0]):
            if pixels[self.x][self.y + 1] == 0:
                return True, 0, 1
            if self.frame % 2 == 0:
                if self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1] == 0:
                    return True, 1, 1
                elif self.x - 1 > -1 and pixels[self.x - 1][self.y + 1] == 0:
                    return True, -1, 1
                elif self.x + 1 < len(pixels) and pixels[self.x + 1][self.y] == 0:
                    return True, 1, 0
                elif self.x - 1 > -1 and pixels[self.x - 1][self.y] == 0:
                    return True, -1, 0
            else:
                if self.x - 1 > -1 and pixels[self.x - 1][self.y + 1] == 0:
                    return True, -1, 1
                elif self.x + 1 < len(pixels) and pixels[self.x + 1][self.y + 1] == 0:
                    return True, 1, 1
                elif self.x - 1 > -1 and pixels[self.x - 1][self.y] == 0:
                    return True, -1, 0
                elif self.x + 1 < len(pixels) and pixels[self.x + 1][self.y] == 0:
                    return True, 1, 0
        return False, 0, 0
    def move(self, pixels, frame):
        moveable, x, y = self.canMove(pixels)
        if self.frame == frame:
            return
        if moveable:
            for a in range(self.x - 1, self.x + 2):
                for b in range(self.y - 1, self.y + 2):
                    if a > 0 and a < len(pixels) and b > 0 and b < len(pixels[0]):
                        if pixels[a][b] != 0:
                            if pixels[a][b].static == True:
                                pixels[a][b].static = False
            self.x += x
            self.y += y
            self.frame = frame
            pixels[self.x][self.y] = self
            pixels[self.x - x][self.y - y] = 0
    def draw(self, pg, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, 1, 1))

