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


    # Rectオブジェクトは(x, y, w, h)の情報を持ち、移動メソッドmove_ipを持つ
    kk_rct = kk_ing.get_rect()
    kk_rct.center = 300, 200 # 初期位置設定
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed()
        
        # 1-1
        # こうかとんが左に流れる速度(-1, 0) とする
        dx, dy = -1, 0 
        
        # 右矢印キーが押されているかどうかのフラグ
        is_right_pressed = key_states[pg.K_RIGHT]
        
        # 1-2：ー操作による移動量の計算
        # K_UP, K_DOWN, K_LEFT の操作を定義
        if key_states[pg.K_UP]:
            dy = -5
        if key_states[pg.K_DOWN]:
            dy = 5
        if key_states[pg.K_LEFT]:
            dx = -5

        # 課題1-2：右矢印キーの操作
        if key_states[pg.K_RIGHT]:
            dx = 5

       
            

        # move_ip メソッドの使用を1回だけにする
        kk_rct.move_ip(dx, dy) 

        X = tmr % 800  # 800ピクセルごとにループ
        
        # 背景画像の描画 (背景画像は左へスクロールしているように見える)
        screen.blit(bg_img, [-X, 0])
        screen.blit(bg2_ing, [-X - 1600, 0])
        
        # こうかとんの表示。kk_rct の位置情報を使用して表示する
        screen.blit(kk_ing, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
