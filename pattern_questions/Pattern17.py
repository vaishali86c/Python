def Func():
    n = 5
    for i in range(n):
        # space
        for j in range(n - i - 1):
            print(" ", end="")
        
        # alphabetical number - increase (0 to i)
        for k in range(i + 1):
            print(chr(65 + k), end="")
        
        # decrease (i - 1 to 0)
        for k in range(i - 1, -1, -1):
            print(chr(65 + k), end="")
        
        # # space
        # for i in range(n - i - 1):
        #     print(" ", end="")
        print()
Func()

#     A    
#    ABC   
#   ABCBA 
#  ABCDCBA
# ABCDEDCBA