class Solution:
    def reverseNumber(self, n):
        # init a number to store reverse number
        revNum = 0

        while n > 0:
            # gives last digit
            lastdigit = n % 10
            # reverse : extract last digit and reverse means multiply rev num by 10 and add extracted digit
            revNum = revNum * 10 + lastdigit
            # remove last digit
            n = n // 10
        return revNum
    
obj = Solution()
num = 12345
print("Number:", num)
print("Reverse Number:", obj.reverseNumber(num))


