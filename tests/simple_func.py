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

student = []
while True:
    score = int(input("Enter score, enter 0 to exit: "))
    if score == 0:
        break
    else:
        student.append(score)
analyze_grade(student)