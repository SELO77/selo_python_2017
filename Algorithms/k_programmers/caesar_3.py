def caesar(s, n):
    result = ""
    for c in s:
        # print('c', c)
        if c.isalpha():
            asci = ord(c) + n
            if c.isupper():
                # 65 - 90
                if asci > 90:
                    asci = 65 + (asci - 91)
                result += chr(asci)
            else:
                # 97 - 122
                if asci > 122:
                    asci = 97 + (asci - 123)
                result += chr(asci)
        elif c.isspace():
            result += c
        else:
            continue
    print('s:', s)
    print('result:', result)
    return result
    # 주어진 문장을 암호화하여 반환하세요.

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4)) # e F d
print('s는 "a B z", n은 4인 경우: ' + caesar("YMiStPRQNIUcMuQd EehtmPqV  XyPYRiFJhtFDYsAaNocTnp", 15))


import random


def test_caesar():
    sample_set = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [' !@#']
    test_data = ''
    random_num = random.randrange(5, 20)
    for i in range(random.randrange(5, 20)):
        test_data += random.sample(sample_set)

    result = caesar(sample_set, random_num)
    print(result)


