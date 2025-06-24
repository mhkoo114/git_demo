# Name & age level
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

if age < 0:
    print("Please enter a valid age.\n")
elif 0 <= age <= 12:
    print("You are a child.\n")
elif 13 <= age <= 19:
    print("You are a teenager.\n")
elif 20 <= age <= 59:
    print("You are an adult.\n")
else:
    print("You are a senior citizen.\n") 

# Sum of two number
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a + b

print(f"{a} + {b} = {c}\n")

# Determine odd or even number
numm1 = int(input("Enter a number: "))

if numm1 % 2 == 0:
    print("This is an even number\n")
else:
    print("This is a odd number\n")
 
# Divide calculator
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a factor for the number: "))
final = number1 / number2

print(f"{number1} divide by {number2} equals to {final}\n")

# Sum, Minus, Multiply, divide
print("1 for sum, 2 for minus, 3 for multiply, 4 for divide")
caltype = int(input("Choose either one: "))

if caltype == 1:
    numb1 = float(input("Enter first number: "))
    numb2 = float(input("Enter second number: "))
    finum = numb1 + numb2
    print(f"{numb1} + {numb2} equal to {finum}\n")
if caltype == 2:
    numb1 = float(input("Enter first number: "))
    numb2 = float(input("Enter second number: "))
    finum = numb1 - numb2
    print(f"{numb1} - {numb2} equals to {finum}\n")
if caltype == 3:
    numb1 = float(input("Enter first number: "))
    numb2 = float(input("Enter second number: "))
    finum = numb1 * numb2
    print(f"{numb1} * {numb2} equals to {finum}\n")
if caltype == 4:
    numb1 = float(input("Enter first number: "))
    numb2 = float(input("Enter second number: "))
    finum = numb1 / numb2
    print(f"{numb1} / {numb2} equals to {finum}\n")
    
# Function to get the largest, smallest, and middle values
def get_values(num1, num2, num3):
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    middle = num1 + num2 + num3 - largest - smallest

    return largest, smallest, middle

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest, smallest, middle = get_values(num1, num2, num3)

print(f"A: Largest value is {largest:.2f}")
print(f"B: Smallest value is {smallest:.2f}")
print(f"C: Middle value is {middle:.2f}\n")

def get_color_input():
    while True:
        color = input("Enter color (Y for Yellow, R for Red, B for Blue): ").upper()

        if color in ['Y', 'R', 'B']:
            return color
        else:
            print("Invalid input. Please enter Y, R, or B.")

def mix_colors(color1, color2):
    if (color1 == 'Y' and color2 == 'R') or (color1 == 'R' and color2 == 'Y'):
        print("Orange")
    elif (color1 == 'Y' and color2 == 'B') or (color1 == 'B' and color2 == 'Y'):
        print("Green")
    elif (color1 == 'R' and color2 == 'B') or (color1 == 'B' and color2 == 'R'):
        print("Purple")
    else:
        print("Invalid combination")
def main():
    print("Color Mixing Program")
    color1 = get_color_input()
    color2 = get_color_input()
    mix_colors(color1, color2)

if __name__ == "__main__":
    main()