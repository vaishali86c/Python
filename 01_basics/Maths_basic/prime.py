def prime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt == 2

num = 12

isPrime = prime(num)

if isPrime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
