# simple python loops
"""
for i in range(1, 10):
    print(i, end=" ")   
    # self-defined what ends the line, default is go to next line

######################################################

num = 1
while num <= 10:
    print(num, end=" ")
    num+=1
print("Loop end")

########################################################

start = int(input("Enter starting number: "))
while start > 0:
    print(start, end=" ")
    start-=1
print("Liftoff")

#########################################################

total, count = 0, 0
while True:
    score = int(input("Enter score(0-100, -1 to stop program): "))
    if score == -1:
        break
    elif 0 <= score <= 100:
        total += score
        count += 1
    else:
        print("Invalid score, please try again.")
# if ends immediately the code will crash(ZeroDivisionError)
# so add if count > 0
if count > 0:
    avr = total / count
    print(f"You entered {count} valid scores.")
    print(f"Average score: {avr:.2f}")

###########################################################

for i in range(2,22,2):
    print(i,end=" ")
even = list(range(2,21,2))
print(*even)

############################################################

total = 0
for i in range(1,51):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz-Buzz",end=" ")
    elif i % 3 == 0:
        print("Fizz",end=" ")
        total+=i
    elif i % 5 == 0:
        print("Buzz",end=" ")
        total+=i
    else:
        print(i,end=" ")
print(f"\nTotal sum of numbers divisible by 3 or 5: {total}")

######################################################################

num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

#################################################################
        
count = 0
for num in range(2, 101,):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count+=1
        if count == 5:
            print()
            count = 0
########################################################################

sum = 0
plus = 0
while plus <=100:
    sum+=plus
    plus+=1
print(sum)

############################################################################

name = "itheima is a brand of itcast"
count = 0
for a in name:
    if a == "a":
        count+=1
print(count)

#################################################################################

num, count = 100, 0
for i in range(1,num):
    if i % 2 == 0:
        count+=1
print(count)    # should be 49 even num not include 100

#############################################################################

"""
