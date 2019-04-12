import pyhash

bit_vector =[0]*20
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

fnv_hello = fnv('Hello')%20
murmur_hello = murmur('Hello')%20

bit_vector[fnv_hello] = bit_vector[murmur_hello] = 1
# print(bit_vector)
fnv_world = fnv('World')%20
murmur_world = murmur('World')%20

bit_vector[fnv_world] = bit_vector[murmur_world] = 1
print(bit_vector)