import socket
s= socket.socket()
s.connect(('localhost', 8080))
s.send(b'Hello Socket')
s.send(b'Hello World!')

print('==========')
# print(s.recv(100))