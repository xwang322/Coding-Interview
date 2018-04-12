/*
* 婚礼的酒杯摆设 三角形放置 第一行1个 第二行两个，以此类推，灌入n瓶酒 看如何在第(i)行j列的酒杯装了多少酒，注意每个酒杯可能不是满的，要用小数表示, 假设不超过100层
**/
def fillCups(n, i, j):
    if not n:
        return 0
    if n == 1:
        return [1]
    else:
        answer = []
        temp = [n]
        while not all(item <= 1 for item in temp):
            next = []
            for index, amount in enumerate(temp):
                if index == 0:
                    if temp[0]>1:
                        next.append((temp[0]-1)/2.0)
                    else:
                        next.append(0)
                else:
                    if temp[index-1] > 1 and amount > 1:
                        next.append((temp[index-1]-1)/2.0 + (amount-1)/2.0)
                    elif temp[index-1] > 1:
                        next.append((temp[index-1]-1)/2.0)
                    elif amount > 1:
                        next.append((amount-1)/2.0)
                    else:
                        next.append(0)
            if temp[-1] > 1:
                next.append((temp[-1]-1)/2.0)
            else:
                next.append(0)
            for index in range(len(temp)):
                if temp[index] > 1:
                    temp[index] = 1.0
            answer.append(temp)
            temp = next
    answer.append(temp)
    print answer
    if len(answer) >= i+1 and len(answer[i]) >= j+1:
        return answer[i][j]
    return 0

answer = fillCups(8,2,2)
print answer
