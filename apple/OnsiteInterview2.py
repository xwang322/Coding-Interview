'''
Onsite interview round 4, two Indians, give a question, a matrix, n by n, starting from (0,0) find the shortest step to reach(n-1, n-1).
Each matrix[i][j] = k element means that you can jump from (i,j) position either up/down/left/right k steps, not within k steps, exactly k steps.
You cannot jump out of the grid, return -1 if you cannot reach the destination.
First thought is dp, then realize the jump requirement, this is BFS, set up a queue and a set for visited node to save steps. Use Python to code.
My thought is go from the destination, but the interview said both starting from (0,0) or (n-1,n-1) is the same. Actually it is the same.
'''
def ReachDestination(matrix):
    if not matrix or not matrix[0]:
        return -1
    answer = 0
    queue = []
    n = len(matrix)
    visited = set()
    queue.append((n-1, n-1))
    while (0, 0) not in queue:
        tempset = visited
        length = len(queue)
        answer += 1
        i = 0
        while i < length:
            cor = queue.pop(0)
            cor1 = cor[0]
            cor2 = cor[1]
            if (cor1, cor2) in visited:
                continue
            visited.add((cor1, cor2))
            k = matrix[cor1][cor2]
            if cor1 - k >= 0:
                queue.append((cor1-k, cor2))
            if cor1 + k < n:
                queue.append((cor1+k, cor2))
            if cor2 - k >= 0:
                queue.append((cor1, cor2-k))
            if cor2 + k < n:
                queue.append((cor1, cor2+k))
            i += 1
        if tempset == visited:
            return -1
    return answer

# discussion with interviewers, can use either BFS or DFS. complexity, time O(n^2), space O(n^2). This round is OK.
