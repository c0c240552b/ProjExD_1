import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_ing=pg.image.load("fig/pg_bg.jpg")
    bg2_ing=pg.transform.flip(bg2_ing,True,False)
    kk_ing=pg.image.load("fig/3.png")
    kk_ing=pg.transform.flip(kk_ing,True,False)
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        X=tmr
        screen.blti(bg_img, [0, 0])
        screen.blit(bg_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()