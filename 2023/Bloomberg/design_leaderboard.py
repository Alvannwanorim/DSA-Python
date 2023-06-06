import heapq 
class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if not playerId in self.board:
            self.board[playerId] = score
        else:
            self.board[playerId] += score
        
    def top(self, K: int) -> int:
        heap = []
        for scores in self.board.values():
            heapq.heappush(heap, scores)
            if len(heap) > K:
                heapq.heappop(heap)
        
        return sum(heap)

    def reset(self, playerId: int) -> None:
        if playerId in self.board:
            self.board[playerId] = 0


leaderboard =  Leaderboard()
leaderboard.addScore(1,73) #   // leaderboard = [[1,73]];
leaderboard.addScore(2,56) #   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39) #   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51) #   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4) #    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1) #           // returns 73;
leaderboard.reset(1) #         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2) #         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51) #   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3) #           // returns 141 = 51 + 51 + 39;