from functools import lru_cache
# fibonacciCache = {}

@lru_cache(maxsize = 500)
def nthTerm(n):
    # if n in fibonacciCache:
    #     return fibonacciCache[n]
    if n in (1, 2):
        return 1
    return nthTerm(n-1) + nthTerm(n-2)
    # fibonacciCache[n] = value
    # return value

for n in range(1, 1001):
    print(nthTerm(n))