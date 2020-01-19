a=True
payam1="vasl shodi"
while True:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  #iptaraf
    port = 1083
    s.bind((host , port))
    s.listen(5)
    while 1:
        c, addr = s.accept()
        if a:
            print("yeki vasl shod",addr)
            a=False
        payam1=input()
        ms = payam1
        c.send( ms.encode())
        smp=c.recv(1024)
        print(smp.decode(encoding= 'utf-8' , errors= 'strict'))
        c.close()
