import pygame as pg
import pygame.gfxdraw
from sand import sand

def main():
    pg.init()
    display_size = (800, 600)
    resolution = (400, 300)
    pg.display.set_caption("SandSimulation")
    window = pg.display.set_mode(display_size)
    screen = pg.Surface(resolution)
    running = True
    pixels = [[0 for a in range(resolution[1])] for b in range(resolution[0])]
    buffer = [[0 for a in range(resolution[1])] for b in range(resolution[0])]
    clock = pg.time.Clock()
    while running:
        clock.tick(30)
        screen.fill((0,0,0))
        keys = pg.key.get_pressed() 
        if keys[pg.K_w]:
            xM, yM = pg.mouse.get_pos()
            xM = int(xM / (display_size[0]/resolution[0]))
            yM = int(yM / (display_size[1]/resolution[1]))
            buffer[xM][yM] = sand(xM, yM)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # use the buffer to move the sand and draw it to the screen
        for x in range(resolution[0]):
            for y in range(resolution[1]):
                if buffer[x][y] != 0:
                    
                    buffer[x][y].move(buffer[x][y], buffer)
        for x in range(resolution[0]):
            for y in range(resolution[1]):
                if pixels[x][y] != 0:
                    if pixels[x][y].hasMoved:
                        pixels[x][y].hasMoved = False
                    pg.draw.rect(screen, pixels[x][y].color, (x, y, 1, 1))
        pixels = buffer
        scaled_win = pg.transform.smoothscale(screen, window.get_size())
        window.blit(scaled_win, (0, 0))
        pg.display.flip()
    pg.quit()


if __name__ == "__main__":
    main()
