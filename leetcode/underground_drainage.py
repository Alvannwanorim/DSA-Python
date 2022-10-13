from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.inTime = defaultdict(tuple)
        self.outTime = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inTime[id] = (t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.inTime[id]
        totalDifference = t- startTime
        self.outTime[(startStation, stationName)].append(totalDifference)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(startStation,endStation)])/len(self.o[(startStation,endStation)])
