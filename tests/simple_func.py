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
def analyze_grade(data):
    total = 0
    avr = 0
    max,min = data[0], data[0]
    passed, failed = 0,0
    for i in data:
        total+=i
        if i > max:
            max = i
        if i < min:
            min = i
        if i >= 60:
            passed+=1
        else:
            failed+=1
    avr = total / len(data)
    print(f"Average: {avr:.2f}\nHighest: {max}\nLowest: {min}\nPassed: {passed}\nFailed: {failed}")
###########################################################################################################################################################

def check_password(password):
    special_char = "!@#$%^&*"
    # condition check for the password
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_char for c in password)

    if length and has_upper and has_lower and has_special:
        return "Strong password"
    else:
        return "Too weak"
#######################################################################################################################

def check_email(email):     # check email validity
    if email.count("@") != 1:
        return "Invalid"
    username, domain = email.split("@")
    if username == "" or domain == "":
        return "Invalid"
    if '.' not in domain:
        return "Invalid"
    domain_parts = domain.split('.')
    if "" in domain_parts:
        return "Invalid"
    if len(domain_parts) < 2:
        return "Invalid"
    return "Valid"
########################################################################
  
""" 
def func(*args):
    for i in args:
        print(i)

print(func(1, 2, "test", 4, 5))