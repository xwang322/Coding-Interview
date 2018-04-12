class Solution(object):
    def lengthLongestPath(self, input):
        if not input:
            return ''
        answer = 0
        dictionary = {}
        inputlist = input.split('\n')
        for each in inputlist:
            if '.' not in each:
                level = each.count('\t')
                value = len(each.replace('\t',''))
                dictionary[level] = value
            else:
                level = each.count('\t')
                length = sum(dictionary[temp] for temp in dictionary if temp < level) + len(each.replace('\t','')) + level
                answer = max(answer, length)
        return answer
        
