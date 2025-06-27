import random
count = 5
answer = random.randint(1,100)
# print(answer)
print("A random number between 1-100 has generated.")
while count != 0:
    if count == 1:
        print("You have 1 attempt left.")
    else:
        print(f"You have {count} attempts left.")
    guess = int(input("Guess a number?:"))
    if guess > 100 or guess < 1:
        print("Over the range, try again.")
        continue    # prevent waste of an attempt
    elif guess == answer:
        print(f"Correct! The answer is {answer}.")
        print(f"You guessed in {6-count} tries.")
        break
    # absolute value
    elif abs(guess - answer) <= 15:
        print("Very close!")
    elif guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    count-=1
else:
    print("Times up!")
    print(f"The answer is {answer}.")