import pygame as pg
from sand import sand

def main():
    pg.init()
    display_size = (800, 600)
    #resolution = (400, 300)
    pg.display.set_mode(display_size)
    pg.display.set_caption("SandSimulation")
    #window = pg.display.set_mode(resolution)
    running = True
    pixels = [[0 for a in range(display_size[1])] for b in range(display_size[0])]
    while running:
        pg.display.get_surface().fill((0,0,0))
        keys = pg.key.get_pressed() 
        if keys[pg.K_w]:
            xM, yM = pg.mouse.get_pos()
            pixels[xM][yM] = sand(xM, yM)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        for x in range(display_size[0]):
            for y in range(display_size[1]):
                if pixels[x][y] != 0:
                    pixels = pixels[x][y].move(pixels[x][y], pixels)
        for x in range(display_size[0]):
            for y in range(display_size[1]):
                if pixels[x][y] != 0:
                    pg.display.get_surface().set_at((x, y), pixels[x][y].color)
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
