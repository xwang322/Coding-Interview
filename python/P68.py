class Solution(object):
    def fullJustify(self, words, maxWidth):
        temp_list = []
        temp_sum = 0
        answer = []
        for word in words:
            if len(word) + temp_sum + len(temp_list) > maxWidth:
                for i in range(maxWidth - temp_sum):
                    temp_list[i%(len(temp_list)-1 or 1)] += ' '
                answer.append(''.join(temp_list))
                temp_list = []
                temp_sum = 0
            temp_list.append(word)
            temp_sum += len(word)
        return answer + [' '.join(temp_list).ljust(maxWidth)]
            
                