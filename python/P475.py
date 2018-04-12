class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        answer = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            left = heaters[index-1] if index-1 >= 0 else float('-inf')
            right = heaters[index] if index < len(heaters) else float('inf')
            answer = max(answer, min(house-left, right-house))
        return answer