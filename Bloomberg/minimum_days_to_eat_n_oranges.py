class Solution:
    def minDays(self, n: int) -> int:
        dp ={0: 0, 1: 1}
        def dfs(n):
            if n in dp:
                return dp[n]
            
            one = 1 + (n % 2) + dfs(n//2)
            two = 1 + (n % 3) + dfs(n//3)
            dp[n] = min(one, two)
            return dp[n]
        return dfs(n)
sol = Solution()
print(sol.minDays(10))
