DIAL_CODES = [
    (86, 'CHINA'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
]

d1 = dict(DIAL_CODES)
print(d1)
print(d1.keys())

d2 = dict(sorted(DIAL_CODES))
print(d2)
print(d2.keys())
try:
    assert d1 == '111'
except AssertionError as e:
    print(e.__doc__)