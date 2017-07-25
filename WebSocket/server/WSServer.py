# -*-coding : utf-8 -*-
import base64
import hashlib
import re
import struct
import socket
import subprocess
import sys
import threading


def send(client, msg):
    data = bytearray(msg.encode('utf-8'))
    if len(data) > 126:
        data = bytearray([b'\x81', 126]) + bytearray(struct.pack('>H', len(data))) + data
    else:
        data = bytearray([b'\81', len(data)]) + data
    client.send(data)


def recv(client):
    first_byte = bytearray(client.recv(1))[0]
    FIN = (0xFF & first_byte) >> 7
    opcode = (0x0F & first_byte)
    second_byte = bytearray(client.recv(1))[0]
    mask = (0xFF & second_byte) >> 7
    payload_len = (0x7F)

    if opcode >= 3:
        return opcode, bytearray(b'\x00')

    if (payload_len == 126):
        payload_len = struct.unpack_form('>H', bytearray(client.recv(2)))[0]
    elif (payload_len == 127):
        payload_len = struct.unpack_form('>Q', bytearray(client.recv(8)))[0]

    masked_data = bytearray(client.recv(payload_len))

    if mask == 1:
        masking_key = bytearray(client.recv(4))
        data = [masked_data[i] ^ masking_key[i % 4] for i in range(len(masked_data))]
    else:
        data = masked_data

    return opcode, bytearray(data)


def handshake(client):
    request = client.recv(2048)
    m = re.match('[\\w\\W]+Sec-WebSocket-Key: (.+)\r\n[\\w\\W]+\r\n\r\n', request)

    key = m.group(1) + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

    response_header = 'HTTP/1.1 101 Switching protocols\r\n' + \
                      'Upgrade: websocket\r\n' + \
                      'Connection: Upgrade\r\n' + \
                      'Sec-WebSocket-Accept: %s\r\n' + \
                      '\r\n'

    response_header = response_header % ((base64.b64encode(hashlib.sha1(key).digest()),))
    client.send(response_header)


def handle_client(client, addr):
    handshake(client)

    try:
        while True:
            opcode, data = recv(client)

            if opcode == 0x8:
                print 'close frame received'
                break
            elif opcode == 0x1:
                if len(data) == 0:
                    break
                # data = 'Sever data'
                msg = data.decode('utf-8', 'ignore')
                send(client, msg)

                try:
                    output = unicode(subprocess.check_output(msg, stderr=subprocess.STDOUT, shell=True), 'cp949')
                except subprocess.CalledProcessError as cpe:
                    output = unicode(cpe.output, 'cp949')
                print output
                send(client, output)
            else:
                print 'frame not handled : opcode=' + str(opcode) + ' len=' + str(len(data))

    except Exception as e:
        print str(e)
        print str(e.message)

    print 'disconnected'
    client.close()


def start_server(port):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(5)

    while True:
        print 'Waiting for connection on port ' + str(port) + ' ...'
        client, addr = sock.accept()
        print 'Connection form: ' + str(addr)
        threading.Thread(target=handle_client, args=(client, addr)).start()


start_server(8765)
