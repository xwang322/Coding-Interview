'''
最后半小时问了个system design，假设有5billion个分布在全球的停车场sensor，可以不断汇报各个车位是空的还是满的，
设计一个服务能够支持查询离用户最近的5个空车位。
答得一般，最后谈存储的时候对付认为我的schema太浪费空间，卡了，最后提示下才想出来可以用array的index做sensor id
直接存储代表sensor状态的boolean变量，这样就可以直接用单机内存存储所有数据了。
similar to parking design but more close to SD with considerations of system, db and storage, cache......
'''
class Vehicle (object):
    def __init__(self, state, license, location):
        self.state = state
        self.license = license
        self.location = GPS_Location()

class Motorbike(Vehicle):
    def __init__(self, state, license, location, size):
        Vehicle.__init__(self, state, license, location)
        self.size = 1

class Car(Vehicle):
    def __init__(self, state, license, location, size):
        Vehicle.__init__(self, state, license, location)
        self.size = 2

class Truck(Vehicle):
    def __init__(self, state, license, location, size):
        Vehicle.__init__(self, state, license, location)
        self.size = 3

# Abstract spot: spotnumber, row, level, size
# key point, larger size of spot can contain smaller size of vehicles
#Some outside function return the GPS location can be called at this time, GPS_Location
class Spot(object):
    def __init__(self, continent, country, state, city, building, level, row, number, id):
        # building is an address
        self.continent = continent
        self.country = country
        self.state = state
        self.city = city
        self.building = building
        self.level = level
        self.row = row
        self.number = number
        self.taken = False
        self.location = GPS_Location(self.continent, self.country, self.state, self.city, self.building)

    def checkAvailable(self):
        return self.taken == False

    def canFitVehicle(self, vehicle):
        return self.size >= vehicle.type

    def AssignID(self, num):
        self.id = num

# Needs a database backend stores all the information (Mysql as it is not very big)
# Needs to consider the best datastrcture to find the first spot fitting the size of the incoming car
import heapq
import datetime
import time
import math
import os
import collections
class ParkingLot(object):
    # allocate the global parking lots
    # assume 5 continents, 200 countries, 5000 states, 100000 cities, 5000000 buildings, each building with 1000 spots, total 5 billions spots
    def __init__(self):
        self.locations_dictionary = collections.defaultdict(list)
        self.locations_GPS = collections.defaultdicct(list)
        for i in range(5000000000):
            spot = Spot('','','','','','','','', i)
            # This function returns where it stores in the database or file system
            savepath = os.path.dirname(SaveToDB(spot))
            self.location_directionary[i] = (savepath, False)
            if spot.location not in self.locations_GPS:
                self.locations_GPS[spot.location].append(i)
            self.locations_GPS[spot.location].append(i)
        self.cars_location = {}

    def assignSpots(self, vehicle):
        if not vehicle:
            return
        allocate_spot_id = self.findAvaileSpot(vehicle.size, vehicle.location)
        if allocate_spot_id:
            self.locations_dictionary[allocate_spot_id][1] = True
            temp = FetchFromDB(self.locations_dictionary[allocate_spot_id][0])
            temp.taken = True
            os.path.write(savepath, temp)
        else:
            print 'There is no available Spot right now.'
        self.cars_location[vehicle] = allocate_spot_id

    def findAvaileSpot(self, size, location):
        # needs another outside function to calculate GPS distance, less than 5 miles returned
        spots = [spot for spot in self.locations_GPS if GPS_distance(location, spot) <= 5]
        if not spots:
            spots = [spot for spot in self.locations_GPS if GPS_distance(location, spot) <= 20]
            distances = [GPS_distance(spot, location) for spot in spots]
            if not spots:
                return 'There is no spot within 20 miles around where you are now'
            else:
                id_list =  self.locations_GPS[spots[index for index in range(len(distances)) if distances[index] == min(distances)]]
                spots_list = FetchFromDB(self.locations_dictionary[id_list])
                return sorted(spots_list, key=lambda x:(x.level, x.row, x.number)[0]
        else:
            distances = [GPS_distance(spot, location) for spot in spots]
            id_list =  self.locations_GPS[spots[index for index in range(len(distances)) if distances[index] == min(distances)]]
            spots_list = FetchFromDB(self.locations_dictionary[id_list])
            return sorted(spots_list, key=lambda x:(x.level, x.row, x.number)[0]

    def exit(self, vehicle):
        if vehicle not in self.cars_location:
            return 'This vehicle is not in the parking lot.'
        spot_id = self.cars_location[vehicle]
        self.locations_dictionary[spor_id][1] = False
        temp = FetchFromDB(self.locations_dictionary[allocate_spot_id][0])
        temp.taken = False
        os.path.write(savepath, temp)
        del self.cars_location[vehicle]
