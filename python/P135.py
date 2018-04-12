class Solution(object):
    def candy(self, ratings):
        answer = [1]*len(ratings)
        left = 1
        right = 1
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                left += 1
            else:
                left = 1
            answer[i] = left
        for i in range(len(ratings)-2, -1 , -1):
            if ratings[i]>ratings[i+1]:
                right += 1
            else:
                right = 1
            answer[i] = max(right, answer[i])
        return sum(answer)
        