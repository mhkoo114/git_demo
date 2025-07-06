# simple func test
"""
def count_len(data):    # count length instead of len()
    count = 0
    for i in data:
        count+=1
    print(f"Length of {data} is {count}.")
######################################################################################
    
""" 
def check_degree(degree):
    if degree >= 37.5:
        print(f"{degree}, need to be isolated")
    else:
        print(f"{degree}, lower than standard, normal")
    
degree = float(input("Enter to check your degree: "))
check_degree(degree)