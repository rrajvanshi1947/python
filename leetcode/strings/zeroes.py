def trailingZeroes(n):
        if n < 1:
            return 0
        
        def f(n):
            if n == 1:
                return 1
            
            return n*(f(n-1))
        
        num = str(f(n))
        
        i = len(num)-1
        count = 0
        while i > -1:
            if num[i] == '0':
                count += 1
                i -= 1
                continue
            return count

print(trailingZeroes(8401))