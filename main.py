#!usr/bin/env python
"""
The board game Sorry!

TODO: Gray edges should be one big rectangle, save performance
"""

import pygame as pg

# Colors
white = (255, 255, 255)
gray = (128, 128, 128)
light_gray = (211, 211, 211)
black = (0, 0, 0)
yellow = (255, 255, 0)
gold = (219, 172, 52)

# Dimensions
sqr_edge = 45
piece_rad = (sqr_edge) * 0.4

class Player():

    def __init__(self):
        


def main():
    pg.init()
    screen = pg.display.set_mode((720, 720), pg.SCALED)
    pg.display.set_caption("Sorry! game")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(gray)
    #rect = pg.draw.rect(screen, (0,0,0), (0,0,20,20))

    clock = pg.time.Clock()
    playing = True
    while playing:
        clock.tick(60)

        # Handle input events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
        
        # Draw everything
        screen.blit(background, (0, 0))
        pg.draw.rect(screen, black, (sqr_edge, sqr_edge, 15*sqr_edge-sqr_edge, 15*sqr_edge-sqr_edge), 2)

        # Draw outer grid (60 tiles)
        for i in range(0, 15):
            pg.draw.rect(screen, light_gray, (0, i * sqr_edge, sqr_edge, sqr_edge))
            pg.draw.rect(screen, light_gray, (i * sqr_edge, 0, sqr_edge, sqr_edge))
            pg.draw.rect(screen, light_gray, (15 * sqr_edge, i * sqr_edge, sqr_edge, sqr_edge))
            pg.draw.rect(screen, light_gray, (i * sqr_edge, 15 * sqr_edge, sqr_edge, sqr_edge))

            pg.draw.rect(screen, white, (2.5, i * sqr_edge+2.5, sqr_edge-5, sqr_edge-5), 0, 3) # Left edge
            pg.draw.rect(screen, white, (i * sqr_edge+2.5, 2.5, sqr_edge-5, sqr_edge-5), 0, 3) # Top edge
            pg.draw.rect(screen, white, (15 * sqr_edge+2.5, i * sqr_edge+2.5, sqr_edge-5, sqr_edge-5), 0, 3) # Right edge
            pg.draw.rect(screen, white, (i * sqr_edge+2.5, 15 * sqr_edge+2.5, sqr_edge-5, sqr_edge-5), 0, 3) # Bottom edge

        # Draw bottom-right tile
        pg.draw.rect(screen, light_gray, (15 * sqr_edge, 15 * sqr_edge, sqr_edge, sqr_edge))
        pg.draw.rect(screen, white, (15 * sqr_edge+2.5, 15 * sqr_edge+2.5, sqr_edge-5, sqr_edge-5), 0, 3)
        
        # Draw safety zones
        for i in range(1, 6):
            pg.draw.rect(screen, light_gray, (2 * sqr_edge, i * sqr_edge+2.5, sqr_edge, sqr_edge))
            pg.draw.rect(screen, white, ((2 * sqr_edge) + 2.5, i * sqr_edge+2.5, sqr_edge-5, sqr_edge-5), 0, 3)
        
        # Yellow starting circle
        pg.draw.circle(screen, yellow, ((4 * sqr_edge) + (sqr_edge / 2), (sqr_edge/3) + 2 * sqr_edge+2.5), (1.5*sqr_edge))

        pg.draw.circle(screen, gold, (sqr_edge/2, sqr_edge/2), piece_rad)
        # Yellow triangle polygon coords
        #ylw_triangle = [((2*sqr_edge) + 2.5, 6 * sqr_edge+2.5), ]
        #pg.draw.polygon(screen, white, ylw_triangle)




        pg.display.flip()
        pg.time.Clock().tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
