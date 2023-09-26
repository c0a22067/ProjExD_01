import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_2 = pg.transform.flip(bg_img, True, False)
    tmr = 0
    #こうかとんの初期化
    img_lst = []
    main_img = pg.image.load("ex01/fig/3.png")
    #反転
    main_img = pg.transform.flip(main_img, True, False)
    img_lst.append(main_img)
    #10°から2°ずつ動かすためのリストを作成
    main_img = pg.transform.rotozoom(main_img,10, 1.0)
    img_lst.append(main_img)
    main_img = pg.transform.rotozoom(main_img,8, 1.0)
    img_lst.append(main_img)
    main_img = pg.transform.rotozoom(main_img,6, 1.0)
    img_lst.append(main_img)
    main_img = pg.transform.rotozoom(main_img,4, 1.0)
    img_lst.append(main_img)
    main_img = pg.transform.rotozoom(main_img,2, 1.0)
    img_lst.append(main_img)
    main_img = pg.transform.rotozoom(main_img,0, 1.0)
    img_lst.append(main_img)
    count = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_2, [1600-x, 0])
        screen.blit(bg_img, [3200-x,0])

        if count == 0:
            screen.blit(img_lst[0],[300,200])
        elif count == 1:
            screen.blit(img_lst[1],[300, 200])
        elif count == 2:
            screen.blit(img_lst[2],[300, 200])
        elif count == 3:
            screen.blit(img_lst[3],[300, 200])
        elif count == 4:
            screen.blit(img_lst[4],[300, 200])
        elif count == 5:
            screen.blit(img_lst[5],[300, 200])
        elif count == 6:
            screen.blit(img_lst[6],[300, 200])
            count = 0
        pg.display.update()
        count += 1
        tmr += 1
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()