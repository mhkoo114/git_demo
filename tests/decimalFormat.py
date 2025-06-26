import math
# math header file to use accurate pi value
# simple formatting, ,.2f, alignment, percent
radius = float(input("Enter a radius: "))
area = math.pi*(radius*radius)
round_area = round(area, 2)
print(f"Raw value: {area}")
print(f"Rounded area: {round_area}")
print(f"Formatted area: {area:.2f}")

# alignment and percent
a, b = 1, 2.2
c = 0.564
print(f"{a:>6}")
print(f"{b:>10.2f}")
print(f"{c:.2%}")