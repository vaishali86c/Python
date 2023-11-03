try:
    x = int(input("what is x ?"))
    print(f"x is {x}")
except ValueError:
    print("X is not an Integer")