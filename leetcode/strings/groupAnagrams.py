from collections import defaultdict
def groupAnagrams(strs):
    dic = defaultdict(list)

    for item in strs:
        dic[tuple(sorted(item))].append(item)

    return list(dic.values())

a = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(a))
print(sorted('tea'))