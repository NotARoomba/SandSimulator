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
        screen.fill((0,0,0))
        keys = pg.key.get_pressed() 
        xM, yM = pg.mouse.get_pos()
        xM = int(xM / (display_size[0]/resolution[0]))
        yM = int(yM / (display_size[1]/resolution[1]))
        if keys[pg.K_w]:
            pixels[xM][yM] = Water(xM, yM)
        if keys[pg.K_s]:
            pixels[xM][yM] = Sand(xM, yM)
        if keys[pg.K_a]:
            pixels[xM][yM] = Metal(xM, yM)
        if keys[pg.K_SPACE]:
            pixels[xM][yM] = Element(xM, yM)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        move(resolution, pixels, frame)
        draw(resolution, pixels, screen)
        frame+=1
        scaled_win = pg.transform.smoothscale(screen, window.get_size())
        window.blit(scaled_win, (0, 0))
        pg.display.flip()
    pg.quit()
def move(resolution, pixels, frame):
    for x in range(resolution[0]-1, -1, -1):
        for y in range(resolution[1]-1, -1, -1):
            if pixels[x][y].type != VOID:
                pixels[x][y].move(pixels, frame)
def draw(resolution, pixels, screen):
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            if pixels[x][y].type != VOID:
                pixels[x][y].draw(pg, screen)

if __name__ == "__main__":
    main()
