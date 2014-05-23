# Euler Challenge - Problem 2

num1 = 1
num2 = 1
num3 = 1

total = 0

while num1 + num2 < 4000000:
    num3 = num1 + num2

    if num3 % 2 == 0:
        total += num3
    num1 = num2
    num2 = num3
    num3 = 0

print("Total Even Numbers In Fibonache Sequence Is: " + str(total))
        
