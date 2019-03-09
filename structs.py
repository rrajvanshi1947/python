from struct import *

packed_data = pack('iif', 4,8,85.58)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

unpacked_data = unpack('iif', packed_data) # or b'\x04\x00\x00\x00\x08\x00\x00\x00\xf6(\xabB' in place of packed_data
print(unpacked_data)

