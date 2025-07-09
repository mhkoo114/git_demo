name = "Flame Reaver of the Deepest Dark"
age = 17
salary = 2000.0
message = "My name is %s, age %d, average salary is %.2f" %(name, age, salary)
print(message)

print(name[::-1])   # reverse of the string
print(name[0:16:2])   # define the range of character want to print (start from 0, not include end)
arr = name.split("-")
print(arr)
name = name.replace("Flame Reaver", "Khaslana")
print(name)

if "a" in name:
    print("True")
if "k" not in name:
    print("false")