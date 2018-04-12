class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if not gas or len(gas) == 0:
            return -1
        suma = sum(gas)
        sumb = sum(cost)
        if suma < sumb:
            return -1
        index = 0
        temp = 0
        for i in range(len(gas)):
            temp += gas[i] - cost[i]
            if temp < 0:
                temp = 0
                index = i+1
        return index