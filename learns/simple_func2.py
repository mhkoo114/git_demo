"""
# pass function as parameter
# for code below, the passed func determines the computing logic or purpose
# instead of passing data, and data has been defined in test_func
def test_func(compute):
    result = compute(1, 2)
    print(result)

# the different func of different purposes, but no difference in parameters
def add(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x / y

# pass a chosen func
test_func(multiply)

########################################################################
"""
# lambda param: func_body(1 line of code)
# can use only once, in default will return value
def test_func(compute):
    result = compute(1, 2)
    print(result)

# the way to use, just lambda, func name not needed
test_func(lambda x, y: x + y)