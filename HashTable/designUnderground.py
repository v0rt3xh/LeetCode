'''
1396 Design Underground System
Good practice for applying data structures
in an abstract problem.
Credit: Leetcode-Solution @ Leetcode - CN
Fundamental idea:
Use two hash maps,
First one store the user's entry station and entry time
First key: id
Second one store the 'connection' between stations,
Values are total travel time, total number of passengers
Second key: (start station, end station) 
'''
class UndergroundSystem:

    def __init__(self):
        # Init
        self.customer = dict()
        self.stations = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # update customer hash map
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.customer.get(id)
        # notice that the start-end pair may not exist at first
        travel_time, number_customer = self.stations.get((start_station, stationName),
                                                        (0, 0))
        # running sum & running number
        self.stations[(start_station, stationName)] = travel_time + t - start_time, number_customer + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        cur_time, cur_num = self.stations[(startStation, endStation)]
        return cur_time * 1. / cur_num

