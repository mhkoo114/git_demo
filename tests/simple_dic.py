def test():
    return 1, 2

a = test() # return multiple value, will return a dict
print(a)
b, c = test() # use multuple var to receive return of dict
print(b, c)

##############################################

my_dict = {"Name": "Khaslana", "Age": 33550336}
my_dict.keys()
# ["Name", "Age"]
my_dict.values()
# ["Khaslana", 33550336]
my_dict.items()
# [("Name", "Khaslana"), ("Age", 33550336)]

# print(my_dict)
for k,v in my_dict.items():
    print(k)
    print(v)

del my_dict["Age"]
my_dict.clear() # clear the dictionary
# del my_dict       # delete the whole dictionary
print(my_dict)