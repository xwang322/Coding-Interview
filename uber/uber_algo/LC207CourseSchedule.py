class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True
        degree = [0 for i in range(numCourses)]
        for prerequisite in prerequisites:
            degree[prerequisite[0]] += 1
        this_level = []
        next_level = []
        answer = []
        for index, item in enumerate(degree):
            if item == 0:
                this_level.append(index)
        while this_level:
            answer += this_level
            while this_level:
                element = this_level.pop(0)
                for prerequisite in prerequisites:
                    if prerequisite[1] == element:
                        degree[prerequisite[0]] -= 1
                        if degree[prerequisite[0]] == 0:
                            next_level.append(prerequisite[0])
            this_level = next_level
            next_level = []
        if len(answer) == numCourses:
            return True
        else:
            return False