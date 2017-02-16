import zmq

ENCODING_TYPE = 'utf-8'

host = '127.0.0.1'
port = 6879
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect('tcp://%s:%s' % (host, port))
for num in range(1, 6):
    request_str = 'message #%s' % num
    request_bytes = request_str.encode(ENCODING_TYPE)
    client.send(request_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode(ENCODING_TYPE)
    print("send %s, received %s" % (request_str, reply_str))