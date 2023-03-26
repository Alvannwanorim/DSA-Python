from typing import List


def allSum(nums: List[int], target: int) -> List[List[int]]:
    dp = [[] for _ in range(target +1)]

    for n in nums:
        for i in range(1, target + 1):
            if n > i: continue
            if n == i: dp[i].append([n])
            for l in dp[i -n]:
                dp[i].append(l +[n])
    return dp[-1]
print(allSum([1,2,3,4,5],7))
