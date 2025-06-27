numbers = [10,20,30,40]
# print elements in the list
for i in range(4):
    print(numbers[i],end=" ")
# add into last of list
numbers.append(50)
# change second item to 25
numbers[1] = 25
# remove 30
numbers.remove(30)
# print length of the list
print("Length: ", len(numbers))
# print each number in the list
for j in range(len(numbers)):
    print(numbers[j],end=" ")