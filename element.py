VOID = (0, 0, 0)
METAL = (200, 200, 200)
SAND = (253,238,115)
WATER = (0, 0, 255)
class Element:
    def  __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = VOID
        self.frame = 0
    def canMove(self, pixels):
        return False, 0, 0
    def move(self, pixels, frame):
        if self.type == VOID: return
        if self.frame == frame: return
        moveable, x, y = self.canMove(pixels)
        if moveable:
            self.x += x
            self.y += y
            self.frame = frame
            pixels[self.x][self.y] = self
            pixels[self.x - x][self.y - y] = Element(self.x - x, self.y - y)
    def draw(self, pg, screen):
        pg.draw.rect(screen, self.type, (self.x, self.y, 1, 1))
    