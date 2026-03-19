  pattern_questions git:(main) ✗ python3 Pattern11.py
# 1
# 01
# 101
# 0101
# 10101
# 010101
# 1010101
# 01010101
# 101010101

def Func():
    n = 9
    start = 1
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end="")
            start = 1 - start   # for flipping 1 to 0 and 0 to 1
        print()

Func()