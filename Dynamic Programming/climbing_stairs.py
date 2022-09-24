def climbingStairs( n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    memo[n] = climbingStairs( n-1, memo) + climbingStairs(n -2, memo )
    return memo[n]

print(climbingStairs(45))