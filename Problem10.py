# Project Euler - Problem 10

def isPrime(pNum):

    if pNum < 2:
            return False
    if pNum == 2:
        return True
        
    for i in range(3, int(pNum / 2) + 1, 2):
        if pNum % i == 0:
            return False
    return True

# Other version of isPrime()
'''def isPrime(num):
    i = 2

    while i <= num / 2:

        if num % i == 0:
            # Num can be divided by i
            # Return the current number divided by i, which will find any factors of that number
            return True
        i += 1
    return False'''

count = 3
total = 2 # Total starts at 2 because count starts at 3 (2 is the only even prime number, so this program will only check odd numbers. 2 needs to be added at the begining because 2 won't be checked
while count < 2000000:
    if isPrime(count):
        total += count
    count += 2

    if count % 10001 == 0:
        print(str(count))

print("total is " + str(total))
