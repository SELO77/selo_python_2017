#-*- coding: utf-8 -*-
sample0 = u'E😀M🤡😱😽EMOJI👻🙉🐔👺💩🙏🏿🙇🐹😄😃😊☺😉😍😘😚'
sample1 = u'E😀☠'
four_e = u'😀'
three_e = u'☠'

def utf8_char_len_1(c):
        codepoint = ord(c)
        if codepoint <= 0x7f:
            return 1
        if codepoint <= 0x7ff:
            return 2
        if codepoint <= 0xffff:
            return 3
        if codepoint <= 0x10ffff:
            return 4
        raise ValueError('Invalid Unicode character: ' + hex(codepoint))

if __name__ == '__main__':
    print 'run script'
