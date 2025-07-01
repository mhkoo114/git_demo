# automatically remove duplicates, order is not preserved
my_set = {1,2,3,3,4,2,4}
print(my_set)
# convert a list to a set
item = [1,2,2,3,2,4]
unique = set(item)
print(unique)
# convert back to list
unique_list = list(set(item))
print(unique_list)