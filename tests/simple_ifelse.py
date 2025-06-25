# ifelse simple demos
"""
num = int(input("Enter a number: "))
if num > 0:
    print("this is a positive number")
elif num == 0:
    print("this number is 0")
else:
    print("this is a negative number")

###############

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

###############
    
score = int(input("Enter score(0-100): "))
if 0 < score or score > 100:
    print("Invalid score entered, program ended")
elif 90 <= score <= 100:
    print("You got grade A")
elif 80 <= score <= 89:
    print("you got grade B")
elif 70 <= score <= 79:
    print("You got grade C")
elif 60 <= score <= 69:
    print("you got grade D")
else:
    print("you got grade F")
"""
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height*height)
print(f"{bmi:.2f}")     #for testing purpose
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")