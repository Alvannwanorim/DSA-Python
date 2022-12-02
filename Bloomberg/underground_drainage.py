from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.stationTimeRecord = defaultdict(tuple)  
        self.startEndAndTimeRecord = defaultdict(list) 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stationTimeRecord[id] = (t,stationName) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime,startStation = self.stationTimeRecord[id]
        totalTimePerJourney = t- startTime
        self.startEndAndTimeRecord[(startStation, stationName)].append(totalTimePerJourney)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(self.stationTimeRecord)
        print(self.startEndAndTimeRecord)
        return sum(self.startEndAndTimeRecord[(startStation,endStation)])/len(self.startEndAndTimeRecord[(startStation,endStation)])
