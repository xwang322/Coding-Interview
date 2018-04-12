class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not numCourses:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]
        degree = [0]*numCourses
        temp = []
        answer = []
        for prerequisite in prerequisites:
            degree[prerequisite[0]] += 1
        for index, value in enumerate(degree):
            if value == 0:
                temp.append(index)
        while temp:
            current = temp.pop(0)
            for prerequisite in prerequisites:
                if prerequisite[1] == current:
                    degree[prerequisite[0]] -= 1
                    if degree[prerequisite[0]] == 0:
                        temp.append(prerequisite[0])
            answer.append(current)
        if len(answer) == numCourses:
            return answer
        else:
            return []