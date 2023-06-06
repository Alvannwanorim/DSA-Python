import collections
class UndergroundSystem:

    def __init__(self):
        self.travelHistory = collections.defaultdict(list)
        self.stationTravelTime = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if not id in self.travelHistory:
            self.travelHistory[id].append((t, stationName))
        return 


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time, startStation = self.travelHistory[id].pop()
        diff = abs(t - time)
        self.stationTravelTime[(startStation, stationName)].append(diff)
        del self.travelHistory[id]
        return 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not self.stationTravelTime[(startStation, endStation)]: return
        avgTime = sum(self.stationTravelTime[(startStation, endStation)])/ len(self.stationTravelTime[(startStation, endStation)])
        print(avgTime)
        return avgTime
        


# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
undergroundSystem.getAverageTime("Paradise", "Cambridge")
undergroundSystem.getAverageTime("Leyton", "Waterloo")  
undergroundSystem.checkIn(10, "Leyton", 24)
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkOut(10, "Waterloo", 38)
undergroundSystem.getAverageTime("Leyton", "Waterloo")
