
class sand:
    def  __new__(self, x, y):
        self.x = x
        self.y = y
        self.type = 1
        self.color = (255, 255, 255)
        self.hasMoved = False
        return self
    def move(point, pixels):
        if point.hasMoved:
            return
        if point.y + 1 < len(pixels[0]):
            if pixels[point.x][point.y + 1] == 0:
                point.y += 1
                pixels[point.x][point.y - 1] = 0
            elif point.x + 1 < len(pixels) and pixels[point.x + 1][point.y + 1] == 0:
                point.x += 1
                point.y += 1
                pixels[point.x - 1][point.y - 1] = 0
            elif point.x - 1 > -1 and pixels[point.x - 1][point.y + 1] == 0:
                point.x -= 1
                point.y += 1
                pixels[point.x + 1][point.y - 1] = 0
            point.hasMoved = True
            pixels[point.x][point.y] = point
