from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.board = defaultdict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0
        self.board[playerId] += score

    def top(self, K: int) -> int:
        # filter the all the score for each player
        values = [v for _,v in sorted(self.board.items(), keys=lambda item: item[1])]
        # sort the values in reverse order
        values.sort(reverse= True)
        total, i = 0, 0
        while i < K:
            total += values[i]
            i += 1
        return total
    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0