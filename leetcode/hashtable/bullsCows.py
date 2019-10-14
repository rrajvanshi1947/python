class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        arr = []
        dic = {}
        bulls = cows = 0
        for char in secret:
            arr.append(char)
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
            
        for i in range(len(arr)):
            if guess[i] == arr[i]:
                bulls += 1
                
        for char in guess:
            if char in dic and dic[char]:
                cows += 1
                dic[char] -= 1
                
        cows -= bulls
        
        return str(bulls)+"A"+str(cows)+"B"