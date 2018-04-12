'''
Elevator design:
# system design
# OOD
# algorithm
useful link:
https://www.youtube.com/watch?v=DSGsa0pu8-k
https://www.geeksforgeeks.org/design-parking-lot-using-object-oriented-principles/
System design:
1. clarify questions: is this a sd or ood or coding?
2. How is this parking designed? Open space or in a building? How many spots are there, hundreds or thousands, or in different buildings?
3. Does this parking lot have multiple levels? Multiple entrances? (Concurrency related)? Dependencies involved? Fill up certain level in order?
4. Pricing strategy for different size or for different time? (Business side)
5. Premium parking spot or for disability? Valet parking? (Business side)
6. Different sizes of parking spots? (S, M, L, XL)

Starts with 4 sizes of parking spots, small cars can be put into larger size, but not the other way.
Classes need to be defines, vehicles, spots.
'''
# Abstract vehicles: state (string), license plates(string), size is a enum
# car color, year and manufacturer can be mentioned in the interview but not much useful here in this case

# inheritance from class vehicle to motorbike, car, truck, 3 different sizes
class Vehicle (object):
    def __init__(self, state, license):
        self.state = state
        self.license = license

class Motorbike(Vehicle):
    def __init__(self, state, license, size):
        Vehicle.__init__(self, state, license)
        self.size = 1

class Car(Vehicle):
    def __init__(self, state, license, size):
        Vehicle.__init__(self, state, license)
        self.size = 2

class Truck(Vehicle):
    def __init__(self, state, license, size):
        Vehicle.__init__(self, state, license)
        self.size = 3

# Abstract spot: spotnumber, row, level, size
# key point, larger size of spot can contain smaller size of vehicles
class Spot(object):
    def __init__(self, level, row, spotnumber, size):
        self.level = level
        self.row = row
        self.spotnumber = spotnumber
        self.size = size
        self.taken = False

    def checkAvailable(self):
        return self.taken == False

    def canFitVehicle(self, vehicle):
        return self.size >= vehicle.type

    def getRow(self):
        return self.row

    def getspotnumber(self):
        return self.spotnumber

    def getlevel(self):
        return self.level

    def setComeInTime(self, time):
        self.initime = time

# Needs a database backend stores all the information (Mysql as it is not very big)
# Needs to consider the best datastrcture to find the first spot fitting the size of the incoming car
import heapq
import datetime
import time
import math
class ParkingLot(object):
    # assume we have 3 sizes, small, medium, large, with 20, 50, 10 spots each
    # 5 layers, each layer has 4, 10, 2 of each size with 0-index ordering, 2 rows, first row for small and large, second for medium
    # size enum: 1, 2, 3

    def __init__(self):
        self.locations_dictionary = {}
        for i in range(4, -1, -1):
            for j in range(4):
                self.locations_dictionary[(i, 0, j)] = Spot((i, 0, j, 1))
            for k in range(10):
                self.locations_dictionary[(i, 1, k)] = Spot((i, 1, k, 2))
            for l in range(2):
                self.locations_dictionary[(i, 0, 4+l)] = Spot((i, 0, 4+l, 3))
        self.heap1 = []
        self.heap2 = []
        self.heap3 = []
        for i in range(4, -1, -1):
            for j in range(4):
                heapq.heappush(self.heap1, (i, 0, j))
            for k in range(10):
                heapq.heappush(self.heap2, (i, 1, k))
            for l in range(2):
                geapq.heappush(self.heap3, (i, 0, 4+l))
        self.cars_location = {}

    def assignSpots(self, vehicle):
        if not vehicle:
            return
        size = vehicle.size
        allocate_size, allocate_spot = self.findAvailSpot(size)
        if allocate_size and allocate_spot:
            self.locations_dictionary[allocate_spot].setComeInTime(datetime.datetime.now())
            self.locations_dictionary[allocate_spot].taken = True
        else:
            print 'There is no available Spot right now.'
        self.cars_location[vehicle] = allocate_spot


    def findAvailSpot(self, size):
        if size ==  1:
            if self.heap1:
                return [1, heapq.heappop(self.heap1)]
            elif self.heap2:
                return [2, heapq.heappop(self.heap2)]
            elif self.heap3:
                return [3, heapq.heappop(self.heap3)]
            else:
                return [0, False]
        elif size == 2:
            if self.heap2:
                return [2, heapq.heappop(self.heap2)]
            elif self.heap3:
                return [3, heapq.heappop(self.heap3)]
            else:
                return [0, False]
        elif size == 3:
            if self.heap3:
                return [3, heapq.heappop(self.heap3)]
            return [0, False]

    def exit(self, vehicle):
        if vehicle not in self.cars_location:
            return 'This vehicle is not in the parking lot.'
        spot = self.cars_location[vehicle]
        entrance_time = spot.initime
        del self.locations_dictionary[(spot.getlevel, spot.getRow, spot.getspotnumber)]
        if spot.size == 1:
            heapq.heappush(self.heap1, (spot.getlevel, spot.getRow, spot.getspotnumber))
        elif spot.size == 2:
            heapq.heappush(self.heap2, (spot.getlevel, spot.getRow, spot.getspotnumber))
        else:
            heapq.heappush(self.heap3, (spot.getlevel, spot.getRow, spot.getspotnumber))
        exit_time = datetime.datetime.now()
        total_time = (exit_time - entrance_time)/datetime.timedelta(hours=1)
        # assume charing is 2 dollars per hour
        charge = math.ceil(total_time)*2
        return 'You need to pay $ %d dollar', charge
