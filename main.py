import pygame as pg
from element import METAL, Element, VOID, bresenham, circle
from sand import Sand
from water import Water
from metal import Metal


def main():
    pg.init()
    display_size = (800, 600)
    resolution = (400, 300)
    pg.display.set_caption("SandSimulation")
    window = pg.display.set_mode(display_size)
    screen = pg.Surface(resolution)
    running = True
    pixels = [[Element(b, a) for a in range(resolution[1])] for b in range(resolution[0])]
    prev_mouse_pos = (0, 0)
    radius = 3
    frame = 0
    while running:
        screen.fill((0, 0, 0))
        keys = pg.key.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_x = int(mouse_x / (display_size[0] / resolution[0]))
        mouse_y = int(mouse_y / (display_size[1] / resolution[1]))
        if prev_mouse_pos == (0, 0): prev_mouse_pos = (mouse_x, mouse_y)
        element = None
        if keys[pg.K_w]:
            element = Water
        if keys[pg.K_s]:
            element = Sand
        if keys[pg.K_a]:
            element = Metal
        if keys[pg.K_SPACE]:
            element = Element
        if element:
            for i in bresenham(prev_mouse_pos[0], prev_mouse_pos[1], mouse_x, mouse_y):
                if i[0] < resolution[0] and i[1] < resolution[1]:
                    for j in circle(i[0], i[1], radius):
                        if j[0] < resolution[0] and j[1] < resolution[1]:
                            pixels[j[0]][j[1]] = element(j[0], j[1])
        prev_mouse_pos = (mouse_x, mouse_y)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    radius += 1
                if event.button == 5:
                    radius = max(1, radius - 1)
        move(resolution, pixels, frame)
        draw(resolution, pixels, screen)
        frame += 1
        scaled_win = pg.transform.smoothscale(screen, window.get_size())
        window.blit(scaled_win, (0, 0))
        pg.display.flip()
    pg.quit()


def move(resolution, pixels, frame):
    for x in range(resolution[0] - 1, -1, -1):
        for y in range(resolution[1] - 1, -1, -1):
            if pixels[x][y].type != VOID or pixels[x][y].type != METAL:
                pixels[x][y].move(pixels, frame)


def draw(resolution, pixels, screen):
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            if pixels[x][y].type != VOID:
                pixels[x][y].draw(pg, screen)


if __name__ == "__main__":
    main()
