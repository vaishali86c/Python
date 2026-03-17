#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********
# ***********
#  ********* 
#   *******  
#    *****   
#     ***    
#      *    

def Func():
    n = 6
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        for l in range(n - i - 1):
            print(" ", end="")
        print()
    for t in range(n):
        for j in range(t):
            print(" ", end="")
        for k in range(2 * n - (2 * t + 1)):
            print("*", end="")
        for l in range(t):
            print(" ", end="")
        print()

Func()
