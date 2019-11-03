def hammingDistance(x, y):
        a, b = str(bin(x)[2:]), str(bin(y)[2:])
        
        # i = flag = 0
        # if len(a) <= len(b):
        #     i = len(a)-1
        #     flag = 1
        # else:
        #     i = len(b)-1

        i, j = len(a), len(b)
            
        count = 0
        while i > -1 or j > -1:
            if 
            print(a[i], b[i])
            if a[i] != b[j]:
                count += 1
            i -= 1
        print(count)
            
        if flag:
            val = len(b) - len(a) - 1
            while val > -1:
                if b[val]:
                    count += 1
                val -= 1
            print(count)

            return count
        val = len(a) - len(b) - 1
        while val > -1:
            if a[val]:
                count += 1
            val -= 1
        
        print(count)

        return count

print(hammingDistance(4,14))
print(bin(14))