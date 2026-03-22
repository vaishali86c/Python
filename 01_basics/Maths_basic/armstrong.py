def findArmstrongNum(n):
    sum = 0
    orignal = n
    while n > 0:
        lastdigit = n % 10
        sum = sum + (lastdigit * lastdigit * lastdigit)
        n = n // 10
    return sum == orignal

number = 157

if findArmstrongNum(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
