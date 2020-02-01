import pygame
pygame.init()
disp = pygame.display.set_mode((900,550))

# pre variables
end = False
disp_color = (196, 255, 241)
typebox_color = (107, 136, 143)
st = ' '
s = pygame.font.Font('ERASMD.ttf',50)

typebox = s.render(st,True,(0,0,0))
t = 0
mf_read = open('read.txt','r')
mf_print = open('print.txt','r')
ls = [st]
enter = s.render('\n',True,(0,0,0))
# main loop
while not end:
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                st = st[:-1]
                ls[len(ls) - 1] = st
                
            elif event.key == pygame.K_RETURN:
                ls.append(st[t+1:])
                st = ' '
                t = 0
                
            else:
                st += chr(event.key)
                t += 1
                ls[len(ls) - 1] = st
    if not end:


        # shapes
        disp.fill(disp_color)

        pygame.draw.rect(disp,(typebox_color),(100,50,700,65))

        # typing box
        for i in range(len(ls)):
            if i == len(ls) - 1:
                matn = ls[i] + '|'
            else:
                matn = ls[i]
            typebox = s.render(matn,True,(0,0,0))
            disp.blit(typebox,(100,(i + 1) * 50))


        ######
        pygame.display.update()
