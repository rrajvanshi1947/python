class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        
        arr = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        lis = []
        
        for word in words:
            val = -1
            for i in range(len(arr)):
                if word[0].lower() in arr[i]:
                    val = i
                    break
                    
            flag = 0
            for i in range(1, len(word)):
                if word[i].lower() in arr[val]:
                    continue
                else:
                    flag = 1
                    break
            
            if flag == 0:
                lis.append(word)
                
        return lis
            
                
                
        
        