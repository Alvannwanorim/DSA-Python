import collections
from typing import List


class Solution: 
    def bagOfTokensScore(self, tokens: List[int], P: int):
        q = collections.deque(sorted(tokens))
        score = 0
        max_score = 0

        while q:
            if P >= q[0]:
                t = q.popleft()
                P -= t
                score += 1
                max_score = max(score, max_score)
            elif score > 0:
                t = q.pop()
                P += t
                score -= 1
            else:
                break
        return max_score
sol = Solution()
print(sol.bagOfTokensScore([100,200], 150))
                
