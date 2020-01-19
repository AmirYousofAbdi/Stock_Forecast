while True:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  #ip taraf
    port=1083
    s.connect((host, port))
    sms= s.recv(1024)
    print(sms.decode(encoding= 'utf-8' , errors= 'strict'))
    payam2=input()
    md = payam2
    s.send(md.encode())
    s.close()

