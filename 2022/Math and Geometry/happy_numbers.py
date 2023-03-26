
class Solution:
    def isHappy(self,n: int):

        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False
    def sumOfSquares(self, n: int)->int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            print(n, output)
            n = n // 10
        return output
sol = Solution()
print(sol.isHappy(19))