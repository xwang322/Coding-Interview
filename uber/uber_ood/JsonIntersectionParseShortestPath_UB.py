/*
* 上周刚面完店面， 给一个json input，列了一个list的intersection。每个intersection有一个list的road。每条road有通向的intersection，cost和名字。求给一个起始intersection和一个终点intersection，找到最短的路径并且打印出来。
* ex.
* intersection A: [ {name: "road1", cost: 3, destination: "intersection B"}, {name: "road2", cost: 2, destination: "intersection B"}, {name: "road3", cost: 1, destination: "intersection B"} ]
* intersection B: [ {name: "road4", cost: 4, destination: "intersection C"} ]
* intersection C: [][br]
* 最短路径从A到C：road3 -> road4
* 面试官先问如何把这个json转化成数据结构。楼主选择先建一个intersection class和一个road class，然后再用一个HashMap建一个adjacent list。算法是用dfs去搜索。但是楼主最后始终输出的路径不是最短的一条，不知道最后能不能过。。。
**/

class Intersection(object):
    def __init__(self, item):
        for key in item:
            if key == 'cost':
                self.cost = item[key]
            elif key == 'name':
                self.name = item[key]
            elif key == 'destination':
                self.destination = item[key].split()[1]

class RoadClass(object):
    def __init__(self, item):
        for key in item:
            if key == 'cost':
                self.roadcost = item[key]
            elif key == 'name':
                self.roadname = item[key]

import json
import collections
class FindShortestPath(object):

    def __init__(self, intersectionlist):
        self.database = collections.defaultdict(list)
        self.roaddb = {}
        for index, intersection in enumerate(intersectionlist):
            item = json.loads(intersection)
            for each in item:
                self.database[chr(ord('A')+index)].append(Intersection(each))
                self.roaddb[each['name']] = RoadClass(each)
        #for road in self.roaddb:
            #print self.roaddb[road].roadcost, self.roaddb[road].roadname

    def findPath(self, start, destination):
        self.answer = []
        index = 0
        stack = []
        for each in self.database[start]:
            stack.append((each, each.name))
        while stack:
            element, name = stack.pop()
            if element.destination == destination:
                self.answer.append((name))
            if element.destination in self.database:
                for every in self.database[element.destination]:
                    stack.append((every, element.name + ' ' +every.name))
        #print self.answer
        self.path = []
        return self.findMinCost()

    def findMinCost(self):
        answer = float('inf')
        for path in self.answer:
            tempsum = 0
            templist = path.split()
            for temp in templist:
                tempsum += self.roaddb[temp].roadcost
            if tempsum < answer:
                answer = tempsum
                self.path = path
        #print answer
        #print self.path
        return answer

A = ('[{"name": "road1","cost": 3,"destination": "intersection B"}, {"name": "road2","cost": 2,"destination": "intersection B"}, {"name": "road3","cost": 1,"destination": "intersection B"}]')
B = ('[{"name": "road4","cost": 4,"destination": "intersection C"}, {"name": "road5","cost": 7,"destination": "intersection C"}]')
lists = [A, B]
obj = FindShortestPath(lists)
obj.findPath('A','C')
