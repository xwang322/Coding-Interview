class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            return [num for num in range(numCourses)]
        degree = [0 for i in range(numCourses)]
        for pre in prerequisites:
            degree[pre[0]] += 1
        parents = collections.defaultdict(set)
        children = collections.defaultdict(set)
        for pre in prerequisites:
            parents[pre[1]].add(pre[0])
            children[pre[0]].add(pre[1])
        stack = []
        for num in range(numCourses):
            if degree[num] == 0:
                stack.append(num)
        answer = []
        while stack:
            node = stack.pop()
            answer.append(node)
            for each in parents[node]:
                degree[each] -= 1
                children[each].remove(node)
                if not children[each]:
                    del children[each]
                if degree[each] == 0:
                    stack.append(each)
        if not children:
            return answer
        else:
            return []
            
