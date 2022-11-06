from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self) -> None:
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            index = len(self.tweetMap[userId]) - 1
            count, tweetId = self.tweetMap[followeeId][index]
            heapq.heappush(minHeap, [count, tweetId, followeeId, index -1 ])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
