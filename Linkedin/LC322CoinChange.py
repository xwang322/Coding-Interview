class Solution(object):
    def coinChange(self, coins, amount):
        if not amount:
            return 0
        queue = [0]
        next_level = []
        total = 0
        visited = [False for i in range(1+amount)]
        while queue:
            total += 1
            for value in queue:
                for coin in coins:
                    newval = value + coin
                    if newval == amount:
                        return total
                    elif newval > amount:
                        continue
                    else:
                        if not visited[newval]:
                            visited[newval] = True
                            next_level.append(newval)
            queue = next_level
            next_level = []
        return -1
        
