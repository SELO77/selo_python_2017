import zmq


host = "127.0.0.1"
port = 6789
context = zmq.Context()
server = context.socket(zmq.REQ)
server.bind("tcp://%s%s" % (host, port))
while True:
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("Server received: %s" % request_str)
    reply_str = "Stop saying: %s" % request_str
    reply_bytes = bytes(request_str, 'utf-8')
    server.send(reply_bytes)