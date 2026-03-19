# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def Func():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        for k in range(2 * (n - i - 1)):
            print(" ", end="")
        for j in range(i, -1, -1):  # for reverse pattern
            print(j + 1, end="")
        print()

Func()