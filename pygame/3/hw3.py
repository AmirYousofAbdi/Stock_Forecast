import pygame as pg
from random import randint as rm
pg.init()
disp = pg.display.set_mode((600,600))

# pre var
end = False
dog = pg.image.load('doga.png')
dog = pg.transform.scale(dog,(49,51))
cat = pg.image.load('cat.png')
cat = pg.transform.scale(cat,(49,49))
xd = yd = 50
bark = pg.mixer.Sound('bark.wav')
x = y = 0
barkper = False
bd = False
acc = pg.mixer.Sound('Click.wav')

ls = []
for i in range(10):
    ls.append([rm(0,551),rm(0,551)])

#main loop
##while not end:
##    for et in pg.event.get():
##        if et.type == pg.KEYDOWN:
##            if et.key == pg.K_UP:
##                dyd = -1
##            elif et.key == pg.K_DOWN:
##                dyd = 1
##            elif et.key == pg.K_RIGHT:
##                dxd = 1
##            elif et.key == pg.K_LEFT:
##                dxd = -1
##            bd = True
##        else:
##            dxd = dyd = 0
##            bd = False
##        if et.type == pg.MOUSEBUTTONDOWN:
##            x,y = pg.mouse.get_pos()
##            barkper = True
##
##                    
##    #shapes
##    disp.fill((255,255,255))
##    if xd <= x <= xd + 49 and yd <= y <= yd + 51 and barkper:
##        bark.play()
##        barkper = False
##    if 0 <= xd + dxd <= xd + dxd + 49 <= 600 and 0 <= yd + dyd <= yd + dyd + 51 <= 600:
##        xd += dxd
##        yd += dyd
##    
##    disp.blit(dog,(xd,yd))
##    if (xd + 49 == 600 or xd == 0 or yd == 0 or yd + 50 == 600) and bd:
##        acc.play()
##        bd = False
##
##    if ((xc) - (xd + 49) <= 10 and (yc) - (yd + 49) <= 10) or (xd - (xc + 49) <= 10 and yd - (yc + 49) <= 10):
##        
##        xc = rm(0,551)
##        yc = rm(0,551)
##    
##
##    disp.blit(cat,(xc,yc))
##    
##    pg.display.update()
##    pg.time.Clock().tick(600)
'''   soal emtiyazi'''
#main loop
while not end:
    for et in pg.event.get():
        if et.type == pg.KEYDOWN:
            if et.key == pg.K_UP:
                dyd = -1
            elif et.key == pg.K_DOWN:
                dyd = 1
            elif et.key == pg.K_RIGHT:
                dxd = 1
            elif et.key == pg.K_LEFT:
                dxd = -1
            bd = True
        else:
            dxd = dyd = 0
            bd = False
        if et.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            barkper = True

                    
    #shapes
    disp.fill((255,255,255))
    if xd <= x <= xd + 49 and yd <= y <= yd + 51 and barkper:
        bark.play()
        barkper = False
    if 0 <= xd + dxd <= xd + dxd + 49 <= 600 and 0 <= yd + dyd <= yd + dyd + 51 <= 600:
        xd += dxd
        yd += dyd
    
    disp.blit(dog,(xd,yd))
    if (xd + 49 == 600 or xd == 0 or yd == 0 or yd + 50 == 600) and bd:
        acc.play()
        bd = False
    nls = []
    for i in ls:
        disp.blit(cat,(i[0],i[1]))
        xc = i[0]
        yc = i[1]
        if not ((xd <= xc <= xd + 50 <= xc + 50 or xc <= xd <= xc + 50 <= xd + 50) and (yd <= yc <= yd + 50 <= yc + 50 or yc <= yd <= yc + 50 <= yd + 50)):
            nls.append(i)
    ls = nls[:]
    if not ls:
        pg.quit()
        end = True
    pg.display.update()
    pg.time.Clock().tick(600)
