import pygame
pygame.init()
disp = pygame.display.set_mode((900,550))

# pre variables
end = False
disp_color = (196, 255, 241)
typebox_color = (107, 136, 143)
st = ' '
s = pygame.font.Font('Roboto-Regular.ttf',50)

typebox = s.render(st,True,(0,0,0))
typebox2 = s.render(st,True,(0,0,0))
# main loop
while not end:
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                st += 'q'
            elif event.key == pygame.K_w:
                st += 'w'
            elif event.key == pygame.K_e:
                st += 'e'
            elif event.key == pygame.K_r:
                st += 'r'
            elif event.key == pygame.K_t:
                st += 't'
            elif event.key == pygame.K_y:
                st += 'y'
            elif event.key == pygame.K_u:
                st += 'u'
            elif event.key == pygame.K_i:
                st += 'i'
            elif event.key == pygame.K_o:
                st += 'o'
            elif event.key == pygame.K_p:
                st += 'p'
            elif event.key == pygame.K_a:
                st += 'a'
            elif event.key == pygame.K_s:
                st += 's'
            elif event.key == pygame.K_d:
                st += 'd'
            elif event.key == pygame.K_f:
                st += 'f'
            elif event.key == pygame.K_g:
                st += 'g'
            elif event.key == pygame.K_h:
                st += 'h'
            elif event.key == pygame.K_j:
                st += 'j'
            elif event.key == pygame.K_k:
                st += 'k'
            elif event.key == pygame.K_l:
                st += 'l'
            elif event.key == pygame.K_z:
                st += 'z'
            elif event.key == pygame.K_x:
                st += 'x'
            elif event.key == pygame.K_c:
                st += 'c'
            elif event.key == pygame.K_v:
                st += 'v'
            elif event.key == pygame.K_b:
                st += 'b'
            elif event.key == pygame.K_n:
                st += 'n'
            elif event.key == pygame.K_m:
                st += 'm'
            elif event.key == pygame.K_SPACE:
                st += ' '
            elif event.key == pygame.K_1:
                st += '1'
            elif event.key == pygame.K_2:
                st += '2'
            elif event.key == pygame.K_3:
                st += '3'
            elif event.key == pygame.K_4:
                st += '4'
            elif event.key == pygame.K_5:
                st += '5'
            elif event.key == pygame.K_6:
                st += '6'
            elif event.key == pygame.K_7:
                st += '7'
            elif event.key == pygame.K_8:
                st += '8'
            elif event.key == pygame.K_9:
                st += '9'
            elif event.key == pygame.K_0:
                st += '0'
            elif event.key == pygame.K_BACKSPACE:
                st = st[:-1]

   
    if not end:

        # Soucket
        while True:
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()  #ip taraf
            port=1083
            s.connect((host, port))
            sms= s.recv(1024)
            st2 = (sms.decode(encoding= 'utf-8' , errors= 'strict'))

            s.send(st.encode())
            s.close()



        
        # shapes
        disp.fill(disp_color)

        pygame.draw.rect(disp,(typebox_color),(100,50,700,65))
        disp.blit(typebox,(100,50))
        disp.blit(typebox2,True,(0,0,0))
        # typing box
        
        typebox = s.render(st+'|',True,(0,0,0))
        typebox2 = s.render(st2,True,(0,0,0))

        ######
        pygame.display.update()
    
