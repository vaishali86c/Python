def main():
    number = inputs()
    name(number)

def inputs():
    while True:
        n = int(input("Enter a positive number: "))
        if n > 0:
            break
    return n

def name(n):
    for i in range(n):
        print("hello vaishali")

# if __name__ == "__main__":
main()
