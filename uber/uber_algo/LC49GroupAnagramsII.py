class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        dictionary = {}
        for each in strs:
            dictionary[tuple(sorted(each))] = dictionary.get(tuple(sorted(each)), []) + [each]
        return dictionary.values()
