class Solution(object):
    # bfs
    def findOrder(self, numCourses, prerequisites):
        dependence = [[] for i in range(numCourses)]
        dep_num = [0 for i in range(numCourses)]
        for each in prerequisites:
            if each[0] not in dependence[each[1]]:
                dependence[each[1]].append(each[0])
                dep_num[each[0]] += 1
        curr_list = []
        order_list = []
        for i in range(numCourses):
            if dep_num[i] == 0:
                curr_list.append(i)
        count = 0
        while curr_list:
            curr_course = curr_list[0]
            count += 1
            for i in dependence[curr_course]:
                dep_num[i] -= 1
                if dep_num[i] == 0:
                    curr_list.append(i)
            curr_list.remove(curr_course)
            order_list.append(curr_course)
        if count < numCourses:
            return []
        else:
            return order_list