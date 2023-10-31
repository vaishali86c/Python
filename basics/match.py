n = str(input("whats your name ?"))

"""
match n:
    case "harry":
        print("hello harry")
    case "vaishali":
        print("hello vaishali")
    case "sakshi":
        print("hello sakshi")
    case _:
        print("who?")
"""



match n:
    case "harry" | "harrr":
        #        or
        print("hello harry")
    case "vaishali":
        print("hello vaishali")
    case "sakshi":
        print("hello sakshi")
    case _:
        print("who?")