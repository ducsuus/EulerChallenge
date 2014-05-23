# Euler Challenge = Problem 7 - Code used from internet, but explanation is
# custom.

def maxPrimeFactor(num):

    i = 2

    while i <= num / 2:
        
        if num % i == 0:
            
            return maxPrimeFactor(num / i)
        
        i += 1
    # if haven't returned anything by this point, 
    # num must be prime
    return num

print(str(maxPrimeFactor(600851475143)))
