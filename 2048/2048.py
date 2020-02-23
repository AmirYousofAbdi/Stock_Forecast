def turn(num,lspr,dirc):

    if dirc == 1:
        
        for i in range(3,6):
            ls = num[i]
            
            if lspr[i-3][0] and lspr[i-3][1] and ls[0] == ls[1] != ls[2]:  # *|*|0
                
                num[i][0] += num[i][1]
                num[i][1] = 0
                lspr[i-3][1] = False
                num[i-3][1] = style.render('0',True,(0,0,255))
                num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))

            elif lspr[i-3][0] and lspr[i-3][1] and lspr[i-3][2] and ls[0] == ls[1] == ls[2]: # *|*|*

                num[i][0] += num[i][1]
                num[i][2] = 0
                lspr[i-3][2] = False
                num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))
                num[i-3][2] = style.render('0',True,(0,0,255))
                
                
            elif lspr[i-3][1] and lspr[i-3][2] and ls[1] == ls[2] != ls[0]: # 0|*|*
                if lspr[i-3][0]:
                    
                    num[i][1] += num[i][2]
                    num[i][2] = 0
                    lspr[i-3][2] = False
                    num[i-3][2] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                else:
                    
                    num[i][0] = num[i][2] + num[i][1]
                    num[i][2] = 0
                    num[i][1] = 0
                    lspr[i-3][2] = False
                    lspr[i-3][1] = False
                    lspr[i-3][0] = True
                    num[i-3][2] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render('0',True,(0,0,255))
                    num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))
            
            elif not lspr[i-3][1] and num[i][0] == num[i][2] and lspr[i-3][0] and lspr[i-3][2] : # *|*|0
                    
                num[i][0] += num[i][2]
                num[i][2] = 0
                lspr[i-3][2] = False
                num[i-3][2] = style.render('0',True,(0,0,255))
                num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))

            elif lspr[i-3][2]:
                if lspr[i-3][1] and not lspr[i-3][0]:
                    lspr[i-3][2] = False
                    lspr[i-3][0] = True
                    num[i][0] = num[i][1]
                    num[i][1] = num[i][2]
                    
                    num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                elif lspr[i-3][0]:
                    lspr[i-3][1] , lspr[i-3][2] = True,False
                    num[i][1],num[i][2] = num[i][2] , 0
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                    num[i-3][2] = style.render('0',True,(0,0,255))
                elif not lspr[i-3][1] and not lspr[i-3][0]:
                    lspr[i-3][0],lspr[i-3][2] = True,False
                    num[i][0],num[i][2] = num[i][2],0
                    num[i-3][0],num[i-3][2] = style.render(str(num[i][0]),True,(0,0,255)),style.render(str(num[i][2]),True,(0,0,255))
            elif lspr[i-3][1]:
                if not lspr[i-3][2] and not lspr[i-3][0]:
                    lspr[i-3][0],lspr[i-3][1] = True,False
                    num[i][0] , num[i][1] = num[i][1] , 0
                    num[i-3][0] = style.render(str(num[i][0]),True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                    
    #################################
    elif dirc == 2:
        for i in range(3,6):
            ls = num[i]
            
            if lspr[i-3][0] and lspr[i-3][1] and ls[0] == ls[1] != ls[2]:
                if lspr[i-3][2]:
                    
                    num[i][1] += num[i][0]
                    
                    num[i][0] = 0
                    lspr[i-3][0] = False
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                else:
                    num[i][2] = num[i][0] + num[i][1]
                    num[i][0] = 0
                    num[i][1] = 0
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render('0',True,(0,0,255))
                    lspr[i-3][0] = False
                    lspr[i-3][1] = False
                    lspr[i-3][2] = True
                    num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
                
            elif lspr[i-3][1] and lspr[i-3][2] and ls[1] == ls[2] != ls[0]:
                
                num[i][2] += num[i][1]
                
                if lspr[i-3][0]:
                    
                    num[i][1] = num[i][0]
                    num[i][0] = 0
                    lspr[i-3][0] = False
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                else:
                    
                    num[i][0] = num[i][1] = 0
                    lspr[i-3][0] = lspr[i-3][1] = False
                    num[i-3][0] = num[i-3][1] = style.render('0',True,(0,0,255))

                num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
            elif lspr[i-3][0] and lspr[i-3][2] and ls[0] == ls[2] != ls[1] and not lspr[i-3][1]:
                num[i][2] += num[i][0]
                num[i][0] = 0
                num[i-3][0] = style.render('0',True,(0,0,255))
                lspr[i-3][0] = False
                num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
            elif lspr[i-3][0] and lspr[i-3][1] and lspr[i-3][2] and ls[0] == ls[1] == ls[2]:
                num[i][2] += num[i][1]
                num[i][1] = num[i][0]
                num[i][0] = 0
                lspr[i-3][0] = False
                num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
                num[i-3][0] = style.render('0',True,(0,0,255))


            elif lspr[i-3][0]:
                if lspr[i-3][1] and not lspr[i-3][2]:
                    lspr[i-3][2] , lspr[i-3][0] = True,False
                    num[i][0],num[i][1],num[i][2] = 0,num[i][0],num[i][1]
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))
                    num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
                elif lspr[i-3][2] and not lspr[i-3][1]:
                    lspr[i-3][0],lspr[i-3][1] = False,True
                    num[i][0],num[i][1] = 0,num[i][0]
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][1] = style.render(str(num[i][1]),True,(0,0,255))

                elif not lspr[i-3][1] and not lspr[i-3][2]:
                    lspr[i-3][0],lspr[i-3][2] = False,True
                    num[i][0],num[i][2] = 0 , num[i][0]
                    num[i-3][0] = style.render('0',True,(0,0,255))
                    num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))

            elif lspr[i-3][1]:
                if not lspr[i-3][2] and not lspr[i-3][0]:
                    lspr[i-3][1],lspr[i-3][2] = False,True
                    num[i][1],num[i][2] = 0,num[i][1]
                    num[i-3][1] = style.render('0',True,(0,0,255))
                    num[i-3][2] = style.render(str(num[i][2]),True,(0,0,255))
                    
        ##################################
    elif dirc == 3:
        for i in range(3,6):
            i -= 1
            if lspr[0][i-3] and lspr[1][i-3] and num[3][i-3] == num[4][i-3] != num[5][i-3]:
                if lspr[2][i-3]:
                    # por bashad
                    
                    num[3][i-3] += num[4][i-3]
                    num[4][i-3] = num[5][i-3]
                    num[5][i-3] = 0
                    lspr[2][i-3] = False
                    num[2][i-3] = style.render('0',True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                else:
                    #khali bashad
                    num[3][i-3] += num[4][i-3]
                    num[4][i-3] = 0
                    num[1][i-3] = style.render('0',True,(0,0,255))
                    lspr[1][i-3] = False
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
            elif lspr[0][i-3] and lspr[2][i-3] and not lspr[1][i-3]:
                if num[3][i-3] == num[5][i-3]:
                    num[3][i-3] += num[5][i-3]
                    num[5][i-3] = 0
                    num[2][i-3] = style.render('0',True,(0,0,255))
                    lspr[2][i-3] = False
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                else:
                    num[4][i-3] = num[5][i-3]
                    num[5][i-3] = 0
                    lspr[2][i-3] = False
                    lspr[1][i-3] = True
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[2][i-3] = style.render('0',True,(0,0,255))


            elif lspr[1][i-3] and lspr[2][i-3]:
                if lspr[0][i-3] and num[4][i-3] == num[5][i-3] != num[3][i-3]:
                    num[4][i-3] += num[5][i-3]
                    num[5][i-3] = 0
                    num[2][i-3] = style.render('0',True,(0,0,255))
                    lspr[2][i-3] = False
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                elif not lspr[0][i-3] and num[4][i-3] == num[5][i-3] != num[3][i-3]:
                    num[3][i-3] = num[4][i-3] + num[5][i-3]
                    num[4][i-3] = num[5][i-3] = 0
                    num[1][i-3] = num[2][i-3] = style.render('0',True,(0,0,255))
                    lspr[1][i-3] = lspr[2][i-3] = False
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                    lspr[0][i-3] = True
                elif not lspr[0][i-3] and num[4][i-3] != num[5][i-3]:
                    num[3][i-3] , num[4][i-3] = num[4][i-3] , num[5][i-3]
                    lspr[0][i-3] = True
                    lspr[2][i-3] = False
                    num[2][i-3] = style.render('0',True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
            elif lspr[2][i-3] and num[5][i-3] == num[4][i-3] == num[3][i-3]:
                num[3][i-3] += num[4][i-3]
                num[4][i-3] = num[4][i-3]
                num[5][i-3] = 0
                lspr[2][i-3] = False
                num[2][i-3] = style.render('0',True,(0,0,255))
                num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))

            elif lspr[2][i-3]:
                if lspr[1][i-3] and not lspr[0][i-3]:
                    lspr[0][i-3],lspr[2][i-3]= True,False
                    num[3][i-3],num[4][i-3],num[5][i-3] = num[4][i-3],num[5][i-3],0
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[2][i-3] = style.render('0',True,(0,0,255))
                elif lspr[0][i-3] and not lspr[1][i-3]:
                    lspr[1][i-3],lspr[2][i-3] = True,False
                    num[4][i-3],num[5][i-3] = num[5][i-3],0
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[2][i-3] = style.render('0',True,(0,0,255))
                elif not lspr[0][i-3] and not lspr[1][i-3]:
                    lspr[0][i-3],lspr[2][i-3] = True,False
                    num[3][i-3],num[5][i-3] = num[5][i-3],0
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                    num[2][i-3] = style.render('0',True,(0,0,255))
            elif lspr[1][i-3]:
                if not lspr[0][i-3] and not lspr[2][i-3]:
                    lspr[1][i-3],lspr[0][i-3] = False,True
                    num[4][i-3] , num[3][i-3] = 0,num[4][i-3]
                    num[0][i-3] = style.render(str(num[3][i-3]),True,(0,0,255))
                    num[1][i-3] = style.render('0',True,(0,0,255))
############################################################355lewun5gdliun6gci
    elif dirc == 4:
        for i in range(3,6):
            i -= 1
            if lspr[2][i-3] and lspr[1][i-3] and num[5][i-3] == num[4][i-3] != num[3][i-3]:
                if lspr[0][i-3]:
                    num[5][i-3] += num[4][i-3]
                    num[4][i-3] = num[3][i-3]
                    num[3][i-3] = 0
                    num[0][i-3] = style.render('0',True,(0,0,255))
                    lspr[0][i-3] = False
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                elif not lspr[0][i-3]:
                    num[5][i-3] += num[4][i-3]
                    num[4][i-3] = 0
                    lspr[1][i-3] = False
                    num[1][i-3] = style.render('0',True,(0,0,255))
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))

            elif lspr[2][i-3] and lspr[0][i-3] and not lspr[1][i-3] and num[5][i-3] == num[3][i-3]:
                lspr[0][i-3] = False
                num[5][i-3] += num[3][i-3]
                num[3][i-3] = 0
                num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))
                num[0][i-3] = style.render('0',True,(0,0,255))

            elif lspr[0][i-3] and lspr[1][i-3] and num[3][i-3] == num[4][i-3] != num[5][i-3]:
                if lspr[2][i-3]:
                    lspr[0][i-3] = False
                    num[4][i-3] += num[3][i-3]
                    num[3][i-3] = 0
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[0][i-3] = style.render('0',True,(0,0,255))
                elif not lspr[2][i-3]:
                    num[5][i-3] = num[4][i-3] + num[3][i-3]
                    num[3][i-3] = num[4][i-3] = 0
                    lspr[0][i-3] = lspr[1][i-3] = False
                    lspr[2][i-3] = True
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))
                    num[0][i-3] = num[1][i-3] = style.render('0',True,(0,0,255))
            elif lspr[0][i-3] and num[3][i-3] == num[4][i-3] == num[5][i-3]:
                num[5][i-3] += num[4][i-3]
                num[3][i-3] = 0
                num[0][i-3] = style.render('0',True,(0,0,255))
                lspr[0][i-3] = False
                num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))

            elif lspr[0][i-3]:
                if lspr[1][i-3] and not lspr[2][i-3]:
                    lspr[0][i-3],lspr[2][i-3] = False,True
                    num[3][i-3],num[4][i-3],num[5][i-3] = 0,num[3][i-3],num[4][i-3]
                    num[0][i-3] = style.render('0',True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))
                elif lspr[2][i-3] and not lspr[1][i-3]:
                    lspr[0][i-3],lspr[1][i-3] = False,True
                    num[3][i-3],num[4][i-3] = 0,num[3][i-3]
                    num[0][i-3] = style.render('0',True,(0,0,255))
                    num[1][i-3] = style.render(str(num[4][i-3]),True,(0,0,255))
                elif not lspr[2][i-3] and not lspr[1][i-3]:
                    lspr[0][i-3],lspr[2][i-3] = False,True
                    num[3][i-3],num[5][i-3] = 0,num[3][i-3]
                    num[0][i-3] = style.render('0',True,(0,0,255))
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))
            elif lspr[1][i-3]:
                if not lspr[0][i-3] and not lspr[2][i-3]:
                    lspr[1][i-3],lspr[2][i-3] = False,True
                    num[4][i-3],num[5][i-3] = 0,num[4][i-3]
                    num[1][i-3] = style.render('0',True,(0,0,255))
                    num[2][i-3] = style.render(str(num[5][i-3]),True,(0,0,255))

    x = random(0,2)
    y = random(0,2)
    while lspr[x][y]:
        x = random(0,2)
        y = random(0,2)
    lspr[x][y] = True
    num[x][y] = style.render('1',True,(0,0,255))
    num[x+3][y] = 1


    return num,lspr

def done(lspr,num):
    for i in lspr:
        for k in i:
            if not k:
                return False
    for i in range(3,6):
        if not (num[i][0] != num[i][1] != num[i][2]):
            return False
        if not (num[3][i-3] != num[4][i-3] != num[5][i-3]):
            return False
    return True
            
    


import pygame
from random import randint as random

pygame.init()
disp = pygame.display.set_mode((300,300))
while True:
    # pre var
    x1 = random(0,2)
    y1 = random(0,2)
    x2 = random(0,2)
    y2 = random(0,2)
    end = False
    style = pygame.font.Font('BAUHS93.ttf',40)

    num = [[style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255))],
           [style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255))],
           [style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255)),
           style.render('0',True,(0,0,255))],
           [0,0,0],
           [0,0,0],
           [0,0,0]
        
        ]

    lspr=[[False,False,False],
          [False,False,False],
          [False,False,False]]
    lspr[x1][y1] = True
    lspr[x2][y2] = True
    num[x1][y1] = num[x2][y2] = style.render('1',True,(0,0,255))
    num[x1+3][y1] = 1
    num[x2+3][y2] = 1
    # main loop
    while not end :

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    num,lspr = turn(num,lspr,1)
                elif event.key == pygame.K_RIGHT:
                    num,lspr = turn(num,lspr,2)
                elif event.key == pygame.K_UP:
                    num,lspr = turn(num,lspr,3)
                elif event.key == pygame.K_DOWN:
                    num,lspr = turn(num,lspr,4)
                

        #shapes
        disp.fill((173, 173, 173))
        pygame.draw.rect(disp,(140, 0, 0),(0,0,100,100))
        pygame.draw.rect(disp,(135, 32, 32),(100,0,100,100))
        pygame.draw.rect(disp,(130, 56, 56),(200,0,100,100))
        pygame.draw.rect(disp,(133, 74, 74),(0,100,100,100))
        pygame.draw.rect(disp,(133, 74, 74),(100,100,100,100))
        pygame.draw.rect(disp,(135, 105, 105),(200,100,100,100))
        pygame.draw.rect(disp,(135, 116, 116),(0,200,100,100))
        pygame.draw.rect(disp,(133, 126, 126),(100,200,100,100))
        pygame.draw.rect(disp,(166, 166, 166),(200,200,100,100))


        
        for i in range(3):
            for k in range(3):
                
                if i == 0 and lspr[i][k] and k == 0:
                    disp.blit(num[i][k],(38,27))
                elif i == 0 and lspr[i][k] and k == 1:
                    disp.blit(num[i][k],(138,27))
                elif i == 0 and lspr[i][k] and k == 2:
                    disp.blit(num[i][k],(238,27))
                elif i == 1 and lspr[i][k] and k == 0:
                    disp.blit(num[i][k],(38,127))
                elif i == 1 and lspr[i][k] and k == 1:
                    disp.blit(num[i][k],(138,127))
                elif i == 1 and lspr[i][k] and k == 2:
                    disp.blit(num[i][k],(238,127))
                elif i == 2 and lspr[i][k] and k == 0:
                    disp.blit(num[i][k],(38,227))
                elif i == 2 and lspr[i][k] and k == 1:
                    disp.blit(num[i][k],(138,227))
                elif i == 2 and lspr[i][k] and k == 2:
                    disp.blit(num[i][k],(238,227))
        end = done(lspr,num)
        pygame.display.update()
    style = pygame.font.Font('BAUHS93.ttf',50)
    text = style.render('Game Over',True,(0,0,0))
    style_2 = pygame.font.Font('BAUHS93.ttf',30)
    text_2 = style_2.render('Press ENTER to',True,(0,0,0))
    text_3 = style_2.render('play again!',True,(0,0,0))
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = True
        disp.fill((255,0,0))
        disp.blit(text,(5,10))
        disp.blit(text_2,(20,110))
        disp.blit(text_3,(20,140))
        pygame.display.update()
