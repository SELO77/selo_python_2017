#-*- coding: utf-8 -*-

with open("test.txt", 'w') as f:
    text = "안"
    f.write(text)


with open('test.txt', 'rb') as f:
    text = f.read()
    print(text, type(text))
    text_str = text.decode('utf-8')
    print(text_str)

sixteen = int('AA', 16)
print(sixteen)
print(hex(100))



utf8_b = b'\xec\x95\x88'
decoded_text = utf8_b.decode('utf-8')
