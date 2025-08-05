"""
numbers = [5, 10, 15, 20, 25]
total = 0
for num in numbers:
    total += num
# or: total = sum(numbers)
average = total / len(numbers)
print(total)
print(average)
########################################################3
values = [42, 17, 68, 3, 99, 24]
max_var = max(values)
min_var = min(values)
print(f"Maximum: {max_var}\nMinimum: {min_var}")
#########################################################
nums = [4, 7, 10, 13, 16, 19, 22]
count = 0
for num in nums:
    if num % 2 == 0:
        count+=1
print(f"Number of even numbers: {count}")
#######################################################
"""
items = [1,2,2,3,4,4,4,5]
"""
unique = []
for i in items:
    if i not in unique:
        unique.append(i)
print("Original: ",items)
print('Unique: ',unique)
"""
unique = list(set(items))
print(f"Original: {items}")
print("Unique: ",unique)

items.insert(1, "Test") # insert behind the element defined
print(items)