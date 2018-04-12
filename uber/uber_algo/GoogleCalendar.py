'''
第四轮：Hiring Manager，没用问behavior question。上来先introduce yourself，
然后要求设计一个google calendar，就是给你几个人的busy time slots和一个长度L，然后返回一个大家都available的时间段，
时间段的长度必须大于等于L。就是聊聊思路啥的，楼主比较naive，先假设每个人的schedule已经有序，然后就是merge K ordered lists的做法，
直到找到一个长度至少为L的available time，follow up是如果给的是free time而不是busy time，怎么办，这里楼主想复杂了，
面试官想要的，就是把free time翻转一下变成busy time，然后用之前的办法就行。
'''
def GoogleCalendar(slots, L):
    if not slots or not L:
        return []
    temp = []
    for slot in slots:
        for interval in slot:
            temp.append(interval)
    temp = sorted(temp, key=lambda x:x[0])
    answer = []
    for each in temp:
        if answer and answer[-1][1] >= each[0]-1:
            tmp = answer.pop()
            tmp = (tmp[0], max(each[1], tmp[1]))
            answer.append(tmp)
        else:
            answer.append(each)
    if answer and answer[0][0] >= L:
        return [0, L]
    else:
        for i in range(len(answer)-1):
            if answer[i+1][0]-answer[i][1] >= L:
                return [answer[i][1], answer[i+1][0]]
        if 24 - answer[-1][1] >= L:
            return [answer[-1][1], 24]
        return None

answer = GoogleCalendar([[(1,2), (5,7), (10,12), (15,19)], [(2, 7), (9,20)]], 2)
print answer
