class Solution:
    def printAllDivisiors(self, n):
        # create a list to store a response
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        return res

# create object of a solution class
sol = Solution()

N = 12

result = sol.printAllDivisiors(N)
print("Divisor of", N, ":", result)

