import pygame as pg
from random import randint as rm
pg.init()
disp = pg.display.set_mode((600,600))
end = False
'''    soal 2     '''
##x1 = y1 = 100
##x2 = y2 = 200
##end = False
##deltay1 = deltax1 = deltay2 = deltax2 = 0
##while not end:
##
##    for event in pg.event.get():
##        if event.type == pg.KEYUP:
##            deltay1 = deltax1 = deltay2 = deltax2 = 0
##            
##        if event.type == pg.KEYDOWN:
##            
##            if event.key == pg.K_UP:
##                deltay1 = -1
##                
##            if event.key == pg.K_DOWN:
##                deltay1 = 1
##                
##            if event.key == pg.K_LEFT:
##                deltax1 = -1
##                
##            if event.key == pg.K_RIGHT:
##                deltax1 = 1
##                #####
##            if event.key == pg.K_w:
##                deltay2 = -1
##                
##            if event.key == pg.K_s:
##                deltay2 = 1
##                
##            if event.key == pg.K_a:
##                deltax2 = -1
##                
##            if event.key == pg.K_d:
##                deltax2 = 1            
##        
##    x1 += deltax1
##    x2 += deltax2
##    y1 += deltay1
##    y2 += deltay2
##    disp.fill((255,255,255))    
##    pg.draw.rect(disp,(0,0,0),(x1,y1,50,50))
##    pg.draw.rect(disp,(255,0,0),(x2,y2,50,50))
##
##    pg.display.update()
##    pg.time.Clock().tick(100)
'''    soal 2     '''
##def check(ls,x,y):
##    for i in range(len(ls)):
##
##        xd = int(ls[i][0])
##        yd = int(ls[i][1])
##        if ((xd <= x <= xd + 50) and (yd <= y <= yd + 50)) or ((x <= xd <= x + 50) and (y <= yd <= y + 50)):
##            return False
##    return True
##def change(ls,x,y):
##    for i in range(len(ls)):
##        xd = int(ls[i][0])
##        yd = int(ls[i][1])
##        if (xd <= x <= xd + 50) and (yd <= y <= yd + 50):
##            return i
##    return 0    
##            
##ls = [[rm(0,550),rm(0,550)]]
##
##for i in range(9):
##    x = int(rm(0,550))
##    y = int(rm(0,550))
##    while not check(ls,x,y):
##        x = rm(0,550)
##        y = rm(0,550)
##
##    ls.append([x,y])
##
##t = 0
##deltax1 = 0
##deltay1 = 0
##j = 0
##while not end:
##
##
##    for event in pg.event.get():
##
##        if event.type == pg.KEYUP:
##            deltay1 = deltax1 = 0
##            
##        if event.type == pg.KEYDOWN:
##            
##            if event.key == pg.K_UP:
##                deltay1 = -1
##                j = 1
##                
##            if event.key == pg.K_DOWN:
##                deltay1 = 1
##                j = 2
##                
##            if event.key == pg.K_LEFT:
##                deltax1 = -1
##                j = 3
##                
##            if event.key == pg.K_RIGHT:
##                deltax1 = 1
##                j = 4
##
##
##
##        
##        if event.type == pg.MOUSEBUTTONDOWN:
##            x , y = pg.mouse.get_pos()
##            t = change(ls,x,y)
##            #print(t)
##    x = ls[t][0]
##    y = ls[t][1]
##
##    for i in range(10):
##        x1 = ls[i][0]
##        y1 = ls[i][1]
##
##        if (x1 == x + 50  and y1 <= y + 50 <= y1 + 50) or (x1 == x + 50  and y  <= y1+50  <= y+50):
##
##            deltay1 = 0
##
##            deltax1 = 0
##                
##        elif (x  == x1 + 50  and y1 <= y + 50 <= y1 + 50) or (x == x1 + 50  and y  <= y1+50  <= y+50):
##
##            deltay1 = 0
##
##            deltax1 = 0
##
##        elif (y1 == y + 50  and x1 <= x + 50 <= x1 + 50) or (y1 == y + 50  and x  <= x1+50  <= x+50):
##
##            deltay1 = 0
##
##            deltax1 = 0
##                
##        elif (y  == y1 + 50  and x1 <= x + 50 <= x1 + 50) or (y == y1 + 50  and x  <= x1+50  <= x+50):
##
##            deltay1 = 0
##
##            deltax1 = 0
##                    
##
##    ls[t][0] += deltax1
##    ls[t][1] += deltay1
##    disp.fill((255,255,255))
##    for k in range(10):
##        i = ls[k]
##        
##        pg.draw.rect(disp,(k * 20,k * 10,k * 5),(i[0],i[1],50 , 50))
##    
##    pg.display.update()
##    pg.time.Clock().tick(60)
'''   soal 3    '''
##ls = []
##for i in range(60):
##    ls.append([rm(5,595),rm(5,595)])
##mode = 0
##time = 0
##deltax = deltay = 0
##while not end:
##    time += 1
##    # events
##    for event in pg.event.get():
##        if event.type == pg.MOUSEBUTTONDOWN:
##            x,y = pg.mouse.get_pos()
##            if 50 <= x <= 150 and 220 <= y <= 320 and mode == 0:
##                mode = 1
##            elif 250 <= x <= 350 and 220 <= y <= 320 and mode == 0:
##                mode = 2
##            elif 450 <= x <= 550 and 220 <= y <= 320 and mode == 0:
##                mode = 3
##        if event.type == pg.QUIT:
##            pg.quit()
##            end = True
##
##            break
##            
##
##
##    
##    # shapes
##    disp.fill((255,255,255))
##    if mode == 0:
##        
##        style = pg.font.Font('BAUHS93.ttf',22)
##        pg.draw.rect(disp,(0,0,0),(50,220,100,100))
##        text = style.render('noob dog',True,(255,255,255))
##        disp.blit(text,(55,254))
##
##        style = pg.font.Font('BAUHS93.ttf',40)
##        pg.draw.rect(disp,(0,0,0),(250,220,100,100))
##        text = style.render('noob',True,(255,255,255))
##        disp.blit(text,(255,245))
##        
##        style = pg.font.Font('BAUHS93.ttf',60)
##        pg.draw.rect(disp,(0,0,0),(450,220,100,100))
##        text = style.render('pro',True,(255,255,255))
##        disp.blit(text,(455,228))
##    elif mode == 3:
##        time += 1
##        ls = ls[:21]
##        nls = []
##        for i in ls:
##            if not (i[0] - 5 <= x <= i[0] + 5 and i[1] - 5 <= y <= i[1] + 5):
##                
##                dltx = rm(-10,10)
##                dlty = rm(-10,10)
##                if 5 <= (i[0] + dltx) <= 595 and 5 <= (i[1] + dlty) <= 595:
##                    
##                    i[0] += dltx
##                    i[1] += dlty
##                else:
##                    i[0] += -(dltx)
##                    i[1] += -(dlty)
##                pg.draw.circle(disp,(255,50,50),(i[0],i[1]),10)
##                nls.append(i)
##            else:
##                time += 1200
##        ls = nls[:]
##
##        if not ls:
##            end = True
##            pg.quit()
##            break
##        
##    elif mode == 2:
##        time += 1
##        ls = ls[:41]
##        nls = []
##        for i in ls:
##            if not (i[0] - 5 <= x <= i[0] + 5 and i[1] - 5 <= y <= i[1] + 5):
##                dltx = rm(-8,8)
##                dlty = rm(-8,8)
##                if 5 <= (i[0] + dltx) <= 595 and 5 <= (i[1] + dlty) <= 595:
##                    
##                    i[0] += dltx
##                    i[1] += dlty
##                else:
##                    i[0] += -(dltx)
##                    i[1] += -(dlty)
##                pg.draw.circle(disp,(255,50,50),(i[0],i[1]),10)
##                nls.append(i)
##            else:
##                time += 1200
##        ls = nls[:]
##        if not ls:
##            end = True
##            pg.quit()
##            break
##
##
##        
##    elif mode == 1:
##        time += 1
##        nls = []
##        for i in ls:
##            if not (i[0] - 5 <= x <= i[0] + 5 and i[1] - 5 <= y <= i[1] + 5):
##                dltx = rm(-4,4)
##                dlty = rm(-4,4)
##                if 5 <= (i[0] + dltx) <= 595 and 5 <= (i[1] + dlty) <= 595:
##                    
##                    i[0] += dltx
##                    i[1] += dlty
##                else:
##                    i[0] += -(dltx)
##                    i[1] += -(dlty)
##                pg.draw.circle(disp,(255,50,50),(i[0],i[1]),10)
##                nls.append(i)
##            else:
##                time += 1200
##        ls = nls[:]
##        if not ls:
##                end = True
##                pg.quit()
##                break
##    pg.display.update()
##    pg.time.Clock().tick(600)
##
##print(time % 600)



