class Solution(object):
    def firstUniqChar(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indices = [s.index(letter) for letter in letters if s.count(letter) == 1]
        return min(indices) if len(indices) > 0 else -1
    # One round pass
    def firstUniqChar(self, s):
        dict1 = {}
        dict2 = collections.defaultdict(list)
        for index, char in enumerate(s):
            if char not in dict1 and char not in dict2:
                dict1[char] = index
            elif char in dict1 and char not in dict2:
                dict2[char].append(dict1[char])
                dict2[char].append(index)
                del dict1[char]
            elif char in dict2:
                dict2[char].append(index)
        return min(dict1.values()) if len(dict1.values())>0 else -1
