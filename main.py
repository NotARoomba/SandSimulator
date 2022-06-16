import pygame as pg
import pygame.gfxdraw
from sand import Sand
from water import Water


def main():
    pg.init()
    display_size = (800, 600)
    resolution = (400, 300)
    pg.display.set_caption("SandSimulation")
    window = pg.display.set_mode(display_size)
    screen = pg.Surface(resolution)
    running = True
    pixels = [[0 for a in range(resolution[1])] for b in range(resolution[0])]
    radius = 1
    frame = 0
    while running:
        screen.fill((0, 0, 0))
        keys = pg.key.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_x = int(mouse_x / (display_size[0] / resolution[0]))
        mouse_y = int(mouse_y / (display_size[1] / resolution[1]))
        if keys[pg.K_s]:
            for x in range(mouse_x - radius, mouse_x + radius):
                for y in range(mouse_y - radius, mouse_y + radius):
                    if 0 < x < resolution[0] and 0 < y < resolution[1]:
                        pixels[x][y] = Sand(x, y)
        if keys[pg.K_SPACE]:
            for x in range(mouse_x - radius, mouse_x + radius):
                for y in range(mouse_y - radius, mouse_y + radius):
                    if 0 < x < resolution[0] and 0 < y < resolution[1]:
                        pixels[x][y] = 0
        if keys[pg.K_w]:
            for x in range(mouse_x - radius, mouse_x + radius):
                for y in range(mouse_y - radius, mouse_y + radius):
                    if 0 < x < resolution[0] and 0 < y < resolution[1]:
                        pixels[x][y] = Water(x, y)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LSHIFT:
                    radius += 1
                if event.key == pg.K_LCTRL:
                    radius -= 1
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
            if pixels[x][y] != 0:
                if not pixels[x][y].static:
                    pixels[x][y].move(pixels, frame)


def draw(resolution, pixels, screen):
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            if pixels[x][y] != 0:
                pixels[x][y].draw(pg, screen)


if __name__ == "__main__":
    main()
