VOID = (0, 0, 0)
METAL = (200, 200, 200)
SAND = (253, 238, 115)
WATER = (0, 0, 255)


def bresenham(x0, y0, x1, y1):
    """
    Bresenham's line algorithm
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def circle(x, y, r):
    for i in range(r):
        for j in range(r):
            if i**2 + j**2 <= r**2:
                yield x + i, y + j


class Element:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = VOID
        self.frame = 0
        self.spread = 0
        self.density = -1

    def can_move(self, pixels):
        return False, 0, 0

    def move(self, pixels, frame):
        if self.type == VOID:
            return
        if self.frame == frame:
            return
        movable, x, y = self.can_move(pixels)
        if movable:
            el = Element
            self.x += x
            self.y += y
            self.frame = frame
            if pixels[self.x][self.y].density < self.density: el = type(pixels[self.x][self.y])
            pixels[self.x][self.y] = self
            pixels[self.x - x][self.y - y] = el(self.x - x, self.y - y)

    def draw(self, pg, screen):
        pg.draw.rect(screen, self.type, (self.x, self.y, 1, 1))
