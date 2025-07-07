money = 100000
name = input("Enter username: ")

def check_saving(show_header):
    if show_header:
        print("--------------Check Saving----------------")
    print(f"User {name},\nYour saving is RM{money}.")

def deposit(num):
    global money
    money += num
    print("--------------Deposit----------------")
    print(f"Saved RM{num} into account.")
    check_saving(False)

def withdraw(num):
    global money
    money -= num
    print("--------------Withdraw----------------")
    print(f"Withdrawed RM{num} from account.")
    check_saving(False)

def main():
    print("--------------Main Menu----------------")
    print(f"Hi {name}, welcome to ATM, please choose an action.")
    print("CHECK SAVING\t[1]\nDEPOSIT\t\t[2]\nWITHDRAW\t[3]\nEXIT ATM\t[4]")
    return input()

while True:
    user_input = main()
    if user_input == "1":
        check_saving(True)
    elif user_input == "2":
        num = int(input("How much you want to save? "))
        deposit(num)
    elif user_input == "3":
        num = int(input("How much you want to withdraw? "))
        withdraw(num)
    elif user_input == "4":
        print("--------------EXIT ATM----------------")
        break
    else:
        print("Invalid action, please try again.")