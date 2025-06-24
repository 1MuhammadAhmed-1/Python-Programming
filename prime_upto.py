def prime(num):
    primes = []
    for i in range(2 , num):
        for j in range(2 , i):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes


num = int(input("Enter a number: "))
print(prime(num))