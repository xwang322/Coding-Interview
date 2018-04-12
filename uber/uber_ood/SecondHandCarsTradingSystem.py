'''
第一轮：problem solving，设计一个二手车交易系统。要注意的地方就是车子有不同的attributes，所以最好用Map去存。
然后面试官说车子有卡车，轿车，什么的，问我怎么处理，我说用java的enum处理，面试官感觉也没很赞同。
然后就是系统得有一个filter，根据用户的筛选条件搜合适的车子。
总之，记得边写边说，多让面试官有feedback可以写。
'''
class Vehicle(object):
    def __init__(self, ID, color, mileague, estimateprice):
        self.id = ID
        self.color = color
        self.mileague = mileague
        self.estimateprice = int(estimateprice[1:])

class Car(Vehicle):
    def __init__(self, ID, color, mileague, estimateprice, cartype):
        Vehicle.__init__(self, ID, color, mileague, estimateprice)
        self.cartype = cartype

class Motorbike(Vehicle):
    def __init__(self, ID, color, mileague, estimateprice, cartype):
        Vehicle.__init__(self, ID, color, mileague, estimateprice)
        self.cartype = cartype

class Truck(Vehicle):
    def __init__(self, ID, color, mileague, estimateprice, cartype):
        Vehicle.__init__(self, ID, color, mileague, estimateprice)
        self.cartype = cartype

class TradingSystem(object):
    def __init__(self):
        self.dictionary = {}
        self.colors = ['Red', 'Black', 'White', 'Green', 'Blue']
        self.types = ['Car', 'Motorbike', 'Truck']

    def LoadCarsInfo(self, cars):
        for car in cars:
            self.dictionary[car.id] = [car.color, car.mileague, car.estimateprice, car.cartype]


    # Design the class so it can support either one condition or multiple conditions together
    def FilterByCondition(self, condition):
        if not condition:
            return
        if len(condition.split()) > 1:
            return self.mergeResult(self.FilterByCondition(each) for each in condition.split())
        else:
            answer = []
            if condition in self.colors:
                for each in self.dictionary:
                    if self.dictionary[each][0] == condition:
                        answer.append(each)
            elif len(condition) > 1 and condition[1:].isdigit() and (condition[0] == '>' or condition[0] == '<'):
                temp = int(condition[1:])
                for each in self.dictionary:
                    if condition[0] == '>':
                        if self.dictionary[each][1] > temp:
                            answer.append(each)
                    else:
                        if self.dictionary[each][1] < temp:
                            answer.append(each)
            elif len(condition) > 1 and condition[0] == '$' and condition[1:].isdigit():
                temp = int(condition[1:])
                if temp > 3000:
                    for each in self.dictionary:
                        if temp-3000 <= self.dictionary[each][2] <= temp+3000:
                            answer.append(each)
                else:
                    for each in self.dictionary:
                        if self.dictionary[each][2] <= 4000:
                            answer.append(each)
            elif condition in self.types:
                for each in self.dictionary:
                    if self.dictionary[each][-1] == condition:
                        answer.append(each)
        return answer

    def mergeResult(self, results):
        answer = self.dictionary.keys()
        for result in results:
            for each in answer:
                if each not in result:
                    answer.remove(each)
        return answer

    def printFilter(self, answer):
        if not answer:
            print 'None of Valid Results'
        else:
            for each in answer:
                print self.dictionary[each]

obj1 = Car(1, 'Red', 30000, '$17000', 'Car')
obj2 = Car(2, 'Blue', 40000, '$9000', 'Car')
obj3 = Motorbike(3, 'Black', 50000, '$7500', 'Motorbike')
obj4 = Truck(4, 'Green', 60000, '$28900', 'Truck')
obj = TradingSystem()
obj.LoadCarsInfo([obj1, obj2, obj3, obj4])
print obj.dictionary
#obj.printFilter(obj.FilterByCondition('Red'))
#obj.printFilter(obj.FilterByCondition('Car'))
#obj.printFilter(obj.FilterByCondition('<50000'))
#obj.printFilter(obj.FilterByCondition('$30000'))
#obj.printFilter(obj.FilterByCondition('<50000 Car'))
