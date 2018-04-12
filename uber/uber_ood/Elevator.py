'''
Elevator, should be OOD design
some useful link:
https://discuss.leetcode.com/topic/119566/design-an-elevator
https://discuss.leetcode.com/topic/94696/design-an-elevator-system/2
第二轮一个ABC（或者ABK），先是问了几个behavior问题，然后就是design elevator，不用写代码就是画图瞎扯。
全程面无表情但会follow up提问题，自我感觉中规中矩吧
'''
def request(currentfloor, destinationfloor):
def PhysicsMoveElevatorUpbyOneFloor():
def PhysicsMoveElevatorDownbyOneFloor():

import collections
class ElevatorController(object):
    def __init__(self, numElevators):
        self.statetable = {}
        self.elevatortable = {}
        for i in range(numElevators):
            self.elevatortable[i] = Elevator(i, 9, 0, 500, 'idle')
            self.statetable[i] = (self.statetable[i].currentfloor, True)
        self.requestQueue = collections.deque([])

    def MoveElevatorUp(self, id, destination):
        self.statetable[id][1] = False
        while not self.statetable[id][1]:
            self.elevatortable[id].MoveUp(destination)
            if self.elevatortable[id].state == 'idle':
                self.statetable[id][1] = True
        return

    def MoveElevatorDown(self, id, destination):
        self.statetable[id][1] = False
        while not self.statetable[id][1]:
            self.elevatortable[id].MoveDown(destination)
            if self.elevatortable[id].state == 'idle':
                self.statetable[id][1] = True
        return

    def ElevatorListener(self, id):
        self.statetable[id][0] = self.elevatortable[id].currentfloor

    def FindAvailable(self, destination):
        candidates = [id in self.statetable if self.statetable[id][1] == True]
        distances = [abs(self.statetable[i][0]-destination) for i in candidates]
        return candidates[distances.index(min(distances))]

    def RequestListener(self, request):
        self.requestQueue.append(request)

    def OperatingTask(self):
        while self.requestQueue:
            currentrequest = self.requestQueue.pop(0)
            assignedid = self.FindAvailable(currentrequest[0])
            self.ElevatorListener(assignedid)
            if self.statetable[assignedid][0] < currentrequest[0]:
                self.MoveElevatorUp(assignedid, currentrequest[0])
                if self.statetable[assignedid][1] == True:
                    self.ElevatorListener(assignedid)
                    if self.statetable[assignedid][0] < currentrequest[1]:
                        self.MoveElevatorUp(assignedid, currentrequest[1])
                    else:
                        self.MoveElevatorDown(assignedid, currentrequest[1])
            elif self.statetable[assignedid][0] > currentrequest[0]:
                self.MoveElevatorDown(assignedid, currentrequest[0])
                if self.statetable[assignedid][1] == True:
                    self.ElevatorListener(assignedid)
                    if self.statetable[assignedid][0] < currentrequest[1]:
                        self.MoveElevatorUp(assignedid, currentrequest[1])
                    else:
                        self.MoveElevatorDown(assignedid, currentrequest[1])
        return 'All tasks finished, currently no job ongoing.'


class Elevator(object):
    def __init__(self, id, maxfloor, minfloor, maxweight, state):
        self.id = id
        self.maxfloor = maxfloor
        self.minfloor = minfloor
        self.maxweight = maxweight
        self.state = state
        self.currentfloor = 0
        self.destination = None

    def GetDirection(self, floor):
        if floor > self.currentfloor:
            return 'Up'
        elif floor < self.currentfloor:
            return 'Down'
        return None

    def MoveUp(self, destination):
        self.destination = destination
        if 'Up' == self.GetDirection(destination):
            self.state = 'moving up'
            while self.currentfloor != self.destination:
                PhysicsMoveElevatorUpbyOneFloor()
                self.currentfloor += 1
            self.state = 'idle'

    def MoveDown(self, destination):
        self.destination = destination
        if 'Down' == self.GetDirection(destination):
            self.state = 'moving down'
            while self.currentfloor != self.destination:
                PhysicsMoveElevatorUpbyOneFloor()
                self.currentfloor -= 1
            self.state = 'idle'

    def CheckAvailability(self):
        return self.state == 'idle'
