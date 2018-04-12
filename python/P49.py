class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        temp_dict = {}
        for each in strs:
            temp_key = tuple(sorted(each))
            temp_dict[temp_key] = temp_dict.get(temp_key, []) + [each]
        return temp_dict.values()
        