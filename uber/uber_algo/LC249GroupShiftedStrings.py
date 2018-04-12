class Solution(object):
    def groupStrings(self, strings):
        dictionary = collections.defaultdict(list)
        for string in strings:
            temp = []
            for i in range(len(string)-1):
                temp.append(str((ord(string[i+1])-ord(string[i]))%26))
            temp = ''.join(temp)
            dictionary[temp].append(string)
        return [dictionary[key] for key in dictionary.keys()]