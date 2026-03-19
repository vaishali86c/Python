# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def Func():
    n = 5
    for i in range(2 * n - 1):
        if i < n:
            stars = i + 1
        else:
            stars = 2 * n - i - 1
        for j in range(stars):
            print("*", end="")
        print()
    
Func()


