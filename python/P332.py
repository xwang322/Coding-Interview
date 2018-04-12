class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            targets[u].append(v)
        answer = []
        self.dfs('JFK', answer, targets)
        return answer[::-1]
    
    def dfs(self, airport, answer, targets):
        while targets[airport]:
            self.dfs(targets[airport].pop(), answer, targets)
        answer.append(airport)
        