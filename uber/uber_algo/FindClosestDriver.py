'''
问题怎么求一个离rider最近的driver，白板写思路，然后上机，自己建图跑test。很简单，秒。留了八分钟谈笑风生讲project，应该是当时最好的一轮。
'''
import math
def FindClosestDriver(rider, drivers):
    if not rider or not drivers:
        return None
    answer = float('inf')
    for driver in drivers:
        distance = (driver[0]-rider[0])**2 + (driver[1]-rider[1])**2
        if distance < answer:
            answer = distance
    return math.sqrt(answer)

answer = FindClosestDriver([4.2, 5.3], [[1.2, 7.8],[2.5, 5.3],[3.4, 6.2],[9.2, 8.9],[10.4, 1.3],[5.2, 4.3]])
print answer
