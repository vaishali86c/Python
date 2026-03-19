def Func():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            start = n - i - 1
            print(chr(65 + start + j), end="")
        print()

Func()

# E
# D E
# C D E
# B C D E 
# A B C D E