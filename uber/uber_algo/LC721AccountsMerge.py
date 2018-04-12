class Solution(object):
    def accountsMerge(self, accounts):
        if not accounts:
            return []
        visited = [False]*len(accounts)
        email_to_id = collections.defaultdict(list)
        answer = []
        for index, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_to_id[account[j]].append(index)
        for index, account in enumerate(accounts):
            if visited[index]:
                continue
            temp = set()
            self.dfs(index, temp, accounts, email_to_id, visited)
            answer.append([account[0]] + sorted(temp))
        return answer

    def dfs(self, index, answer, accounts, dictionary, visited):
        if visited[index]:
            return
        visited[index] = True
        for j in range(1, len(accounts[index])):
            email = accounts[index][j]
            answer.add(email)
            for neighbor in dictionary[email]:
                self.dfs(neighbor, answer, accounts, dictionary, visited)
