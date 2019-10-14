def singleNumber(self, nums):

    if not nums:
        return None
    dic = {}
    for el in nums:
        if el in dic:
            dic.pop(el)
        else:
            dic[el] = 1

    for k, v in dic.items():
        return k
