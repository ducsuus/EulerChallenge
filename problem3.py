# Euler Challenge - Problem 7 (Solved at 02:57 in the morning!)

def maxPrimeFactor(num):

    i = 2

    while i <= num / 2:

        if num % i == 0:
            # Num can be divided by i
            # Return the current number divided by i, which will find any factors of that number
            return maxPrimeFactor(num / i)
        i += 1
    # If this code line is ever reached, the number is a prime number.
    # Should this happen, the number will trace up through the many instances
    # of the macPrimeFactor() code until it reaches the top.
    return num

print(str(maxPrimeFactor(600851475143)))
