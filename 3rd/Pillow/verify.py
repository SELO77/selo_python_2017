from PIL import Image
import magic

i = Image.open("123.jpeg")
print i
try:
    i.load()
except Exception as e:
    print e
    

i = Image.open("error.blob")
print i
try:
    i.load()
except Exception as e:
    print e

print


m = magic.from_file('123.jpeg')
print m

print
with open('123.jpeg', 'rb') as f:
    text = f.read()
    print text[:50]

