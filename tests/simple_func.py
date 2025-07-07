# simple func test
"""
def count_len(data):    # count length instead of len()
    count = 0
    for i in data:
        count+=1
    print(f"Length of {data} is {count}.")
######################################################################################
    
def check_degree(degree):
    if degree >= 37.5:
        print(f"{degree}, need to be isolated")
    else:
        print(f"{degree}, lower than standard, normal")
    
degree = float(input("Enter to check your degree: "))
check_degree(degree)
#########################################################################################

def say_smt():
    print("helllo")

result = say_smt()
print(type(result))
#####################################################################################

def sum_list(num): # sum up item value
    total = 0
    for i in num:
        total+=i
    return total
###########################################################

def factorial(num): # calculate factorial
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
##############################################################################
    
def count_vowels(data): # count vowels
    count = 0
    for i in data:
        if i in "aeiouAEIOU":
            count+=1
    print(count)

def is_palindrome(data):    # identify words like 'racecar'
    reversed_data = data[::-1]
    return data == reversed_data
########################################################################################

""" 

        