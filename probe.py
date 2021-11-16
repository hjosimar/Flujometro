import struct
import codecs
a= b'\xff\xff'
b=codecs.encode(a,'hex')
c=int(b,16)
print(a)
print(b)
print(c)

