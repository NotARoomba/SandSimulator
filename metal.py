from element import *


class Metal(Element):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = METAL
