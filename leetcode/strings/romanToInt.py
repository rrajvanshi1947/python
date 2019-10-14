# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: "III"
# Output: 3
# Example 2:

# Input: "IV"
# Output: 4
# Example 3:

# Input: "IX"
# Output: 9
# Example 4:

# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Optimum Solution
        # rList=['I','V','X','L','C','D','M']
        # rVal=[1,5,10,50,100,500,1000]
        # rDict=dict(zip(rList,rVal))
        # value=0
        # i=0
        # for rname in s:
        #     if (i+1)<len(s):
        #         if s[i]=='I':
        #             if s[i+1]=='V' or s[i+1]=='X':
        #                 value-=2
        #         elif s[i]=='X':
        #             if s[i+1]=='L' or s[i+1]=='C':
        #                 value-=20
        #         elif s[i]=='C':
        #             if s[i+1]=='D' or s[i+1]=='M':
        #                 value-=200
            
        #     value+=rDict[rname]
        #     i+=1
        # return value


        value = 0
        if s[0] == 'I':
            value += 1
        elif s[0] == 'V':
            value += 5
        elif s[0] == 'X':
            value += 10
        elif s[0] == 'L':
            value += 50
        elif s[0] == 'C':
            value += 100
        elif s[0] == 'D':
            value += 500
        elif s[0] == 'M':
            value += 1000
        
        for i in range(1, len(s)):
            if s[i] == 'I':
                value += 1
            elif s[i] == 'V':
                value += 5
            elif s[i] == 'X':
                value += 10
            elif s[i] == 'L':
                value += 50
            elif s[i] == 'C':
                value += 100
            elif s[i] == 'D':
                value += 500
            elif s[i] == 'M':
                value += 1000
                
            if s[i] == 'V' and s[i-1] == 'I':
                value -= 2
            elif s[i] == 'X' and s[i-1] == 'I':
                value -= 2
            elif s[i] == 'L' and s[i-1] == 'X':
                value -= 20
            elif s[i] == 'C' and s[i-1] == 'X':
                value -= 20
            elif s[i] == 'D' and s[i-1] == 'C':
                value -= 200
            elif s[i] == 'M' and s[i-1] == 'C':
                value -= 200
                
        return value
            
        
example = Solution()
print(example.romanToInt('MCMXCIV'))

dic = {'a': 2, "b": 3}
dic = {'c':3}
print(list(dic.values())[0])