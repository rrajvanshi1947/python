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

a = 'Bcsdv'
print(a.isalpha())
print(a)
arr =[]
arr.append([1])
print(arr)
a = ''
if a:
    print('asfd')

