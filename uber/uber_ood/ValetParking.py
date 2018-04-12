'''
Design a valet parking service (OOP question)
useful link:
https://stackoverflow.com/questions/764933/amazon-interview-question-design-an-oo-parking-lot
https://www.careercup.com/question?id=5750856565653504
'''
# There could be many thoughts, I am using one I thought about from the careercup link, including defining multiple class about cars,
# parking ticket, spot and a main class finding the most closest parking lot for some car where the car can fit into that spot.
# 3 different types of lot, 1 2 3 are size.
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

    def SetFree(self):
        self.taken = False

    def getRow(self):
        return self.row

    def getspotnumber(self):
        return self.spotnumber

    def getlevel(self):
        return self.level

    def setComeInTime(self, time):
        self.initime = time

class Ticket(object):
    def __init__(self, id, car, position, valid):
        self.id = id
        self.car = car
        self.position = position
        self.valid = True

    def setInvalid(self):
        self.valid = False

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
        global = 0
        for i in range(5):
            for j in range(4):
                self.locations_dictionary[global] = Spot((i, 0, j, 1))
                global += 1
            for k in range(10):
                self.locations_dictionary[global] = Spot((i, 1, k, 2))
                global += 1
            for l in range(2):
                self.locations_dictionary[global] = Spot((i, 0, 4+l, 3))
                global += 1
        self.heap = []
        for i in range(global):
            heapq.heappush(self.heap, i)
        self.cars_location = {}
        self.tickets = {}
        self.totalTickets = 0
        self.cars_ticket = {}

    def assignSpots(self, vehicle):
        if not vehicle:
            return
        allocate_spot = self.findAvailSpot(vehicle)
        if allocate_spot:
            self.locations_dictionary[allocate_spot].setComeInTime(datetime.datetime.now())
            self.locations_dictionary[allocate_spot].taken = True
        else:
            print 'There is no available Spot right now.'
        self.cars_location[vehicle] = allocate_spot
        self.tickets[self.totalTickets] = Ticket(self.totalTickets, vehicle, allocate_spot, True)
        self.cars_ticket[vehicle] = self.totalTickets
        self.totalTickets += 1

    def findAvailSpot(self, size):
        output = []
        while self.heap:
            temp = heapq.heappop(self.heap)
            if self.locations_dictionary[temp].canFitVehicle:
                return self.locations_dictionary[temp]
            ouput.append(temp)
        for each in output:
            heapq.heappush(self.heap, each)
        return None


    def exit(self, vehicle):
        if vehicle not in self.cars_location:
            return 'This vehicle is not in the parking lot.'
        spot = self.cars_location[vehicle]
        ticketid = self.cars_ticket[vehicle]
        entrance_time = spot.initime
        self.cars_ticket[vehicle].setInvalid()
        self.cars_location[vehicle].SetFree()
        # use id to find spot
        for each in self.locations_dictionary:
            if self.locations_dictionary[each] == spot:
                heapq.heappush(self.heap, each)
        exit_time = datetime.datetime.now()
        total_time = (exit_time - entrance_time)/datetime.timedelta(hours=1)
        # assume charing is 2 dollars per hour
        charge = math.ceil(total_time)*2
        return 'You need to pay $ %d dollar', charge
