a = bytes(3)
print(a)
print(type(a))

b = bytes(b'\xFF\xDD\xdd')
print(b)
print(type(b))

c = bytearray(3)
c[0] = 255
print(c)
print(type(c))