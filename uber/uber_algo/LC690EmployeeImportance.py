"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        #BFS
        '''
        answer = 0
        this_level = []
        next_level = []
        for employee in employees:
            if employee.id == id:
                answer += employee.importance
                this_level += employee.subordinates
        while this_level:
            while this_level:
                employee = this_level.pop(0)
                for temp in employees:
                    if temp.id == employee:
                        answer += temp.importance
                        for each in temp.subordinates:
                            next_level.append(each)
            this_level = next_level
            next_level = []
        return answer
        '''
        #DFS, set up a map is very smart
        dictionary = {e.id:e for e in employees}
        answer = 0
        # this id here is not the built-in function of Python, it is just the parameter from the main function
        stack = [dictionary[id]]
        while stack:
            employee = stack.pop()
            answer += employee.importance
            for each in employee.subordinates:
                stack.append(dictionary[each])
        return answer
