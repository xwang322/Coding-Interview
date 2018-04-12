class Solution(object):
    def groupAnagrams(self, strs):
        if not strs:
            return []
        dictionary = collections.defaultdict(list)
        for eachstr in strs:
            dictionary[tuple(sorted(eachstr))] = dictionary.get(tuple(sorted(eachstr)), [])+[eachstr]
        return dictionary.values()
        
        