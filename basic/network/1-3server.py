import socket
s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(5)
while True:
    print('=======')
    try:
        cs, ca = s.accept()
        print(cs, ca)
        print(cs.recv(100))
        cs.send(b'HaHa')
    except KeyboardInterrupt:
        exit()
    print('=======')