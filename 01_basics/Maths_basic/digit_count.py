def digitCounter(n):
    counter = 0

    while n > 0:
        counter = counter + 1
        # Divide 'n' by 10 to
        # remove the last digit.
        n = n // 10

    return counter

if __name__ == "__main__":
    N = 526736
    print("N:",N)
    digit = digitCounter(N)
    print("Number of Digits in N:", digit)