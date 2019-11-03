def addBinary(a, b):
        # return bin(int(a,2) + int(b,2))[2:]
        
        result = ""
        s = 0
        
        i = len(a)-1
        j = len(b)-1
        
        while (i >= 0 or j >= 0 or s == 1):
            if i >= 0:
                s += int(a[i])
            if j >= 0:
                s += int(b[j])
            
            result = str(s%2) + result
            # print(res)
            
            s //= 2
            i -= 1
            j -= 1
            
        return result

a, b = '11', '1'
print(addBinary(a,b))
print('A'.upper())

# a = 'Bcsdv'
# print(a.isalpha())
# print(a)
# arr =[]
# arr.append([1])
# print(arr)
# a = ''
# if a:
#     print('asfd')

# if val in (1,2) < 3:
#     print('sdkfh')

def add(a, b):

    flag = length = 0
    if len(a) >= len(b):
        flag = 1

    if flag:
        length = len(b)-1
    else:
        length = len(a)-1

    # first = len(a)-1
    # second = len(b)-1

    carry = 0
    string = ''
    while length != -1:
        if a[first] and b[second]:
            if carry:
                string = '1' + string
            else:
                string = '0' + string
            carry = 1
        elif not a[first] and not b[second]:
            if carry:
                string = '1' + string
            carry = 0
        else:
            if carry:
                string = '0' + string
                # carry = 1
            else:
                string = '1' + string

        first -= 1
        second -= 1

    if carry:
