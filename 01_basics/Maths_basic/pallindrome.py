class Solution:
    def pallindromeNum(self, n):
        revNum = 0
        while n > 0:
            lastdigit = n % 10
            revNum = revNum * 10 + lastdigit
            n = n // 10
        return revNum

object = Solution()
Number = 9887
print("Number is:", Number)

if Number == object.pallindromeNum(Number):
    print("Yes, It is pallindrome")
else:
    print("No, It is not pallindrome")