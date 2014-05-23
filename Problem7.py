# Euler Challenge - Problem 7

def isPrime(pNum):
    for i in range(pNum - 1, 2, -1):
        if pNum % i == 0:
            return False
    return True

done = False
num = 0
primeCount = 0
while done == False:

    if isPrime(num):
        print(str(num))
        primeCount += 1
    num += 1

    if primeCount == 1005:
        print("PRIME NUMBER! Allegedly " + str(num))
        done = True
