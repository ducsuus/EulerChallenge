# Euler Problem 1

currentNumbers = []
total = 0

done = False
num = 0
while done == False:
    if num + 3 < 1000:
        num += 3
        currentNumbers.append(num)
        total += num
        print("Multiple Of Three Is " + str(num))
    else:
        done = True

done = False
num = 0
while done == False:
    if num + 5 < 1000:
        num += 5
        print("Multiple Of Five Is " + str(num))
        if num not in currentNumbers:
            total += num
    else:
        done = True

print("Answer is: " + str(total))
print(str(currentNumbers))

    
