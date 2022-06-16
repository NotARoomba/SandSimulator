import pygame as pg
from element import *
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
    frame = 0
    while running:
        screen.fill((0, 0, 0))
        keys = pg.key.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_x = int(mouse_x / (display_size[0] / resolution[0]))
        mouse_y = int(mouse_y / (display_size[1] / resolution[1]))
        if keys[pg.K_w]:
            pixels[mouse_x][mouse_y] = Water(mouse_x, mouse_y)
        if keys[pg.K_s]:
            pixels[mouse_x][mouse_y] = Sand(mouse_x, mouse_y)
        if keys[pg.K_a]:
            pixels[mouse_x][mouse_y] = Metal(mouse_x, mouse_y)
        if keys[pg.K_SPACE]:
            pixels[mouse_x][mouse_y] = Element(mouse_x, mouse_y)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
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
            if pixels[x][y].type != VOID:
                pixels[x][y].move(pixels, frame)


def draw(resolution, pixels, screen):
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            if pixels[x][y].type != VOID:
                pixels[x][y].draw(pg, screen)


if __name__ == "__main__":
    main()
