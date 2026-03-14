# *****
# ****
# ***
# **
# *

def Func():
    n = 6
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()
        n = n - 1
Func()