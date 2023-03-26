class Solution:
    def winnerOfCircularGame(group, num):
        group = list(1, group + 1)
        return 
    def josephus_problem(n, skip):
        skip -= 1
        idx = skip

        while len(n) > 1:
            n.pop(idx)
            idx = (idx + skip) % len(n)
        return n[-1]