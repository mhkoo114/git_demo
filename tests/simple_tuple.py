# ways initializing a tuple
# element in tuple cannot be changed once initialized
mytuple = (1, "Hello", 4, True)
mytuple2 = ()
mytuple3 = tuple()
print(f"mytuple is {type(mytuple)}, content is {mytuple}")

t4 = ("hello")  # only if added a , behind the element, then consider as tuple
t5 = ("world",)
print(f"t4 is {type(t4)}, t5 is {type(t5)}")

t6 = ((1, 2, 3), (3, 4, 5))     # nested tuple is allowed
print(t6[1][-1])    # use a index to get element in tuple
index = mytuple.index("Hello")
print(index)
# index(), count(), len()