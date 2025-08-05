gradebook = [["Name", "Score", "Grade"]]
# function to get grade
def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "c"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
# data input loop
while True:
    print("ENTER 'done' TO FINISH.")
    name = input("Student name: ")
    if name.lower() == "done":
        break
    score = int(input("Enter score: "))
    grade = getGrade(score)
    gradebook.append([name, score, grade])

# ask if user want to edit student
edit_name = input("Want to edit a student's score? Enter name(or 'no')")
if edit_name.lower() != "no":
    found = False
    for i in range(1, len(gradebook)):
        if gradebook[i][0].lower() == edit_name.lower():
            new_score = int(input(f"Enter new mark for {edit_name}: "))
            gradebook[i][1] = new_score
            gradebook[i][2] = getGrade(new_score)
            found = True
            print(f"{edit_name}'s score updated.")
            break
    if not found:
        print("Student not found.")

print("\n----Student Gradebook----")
for row in gradebook:
    for item in row:
        print(str(item).ljust(12),end="")
    print()

# calculate average score excluding header
total = 0
for i in range(1, len(gradebook)):
    total += gradebook[i][1]
average = total / (len(gradebook) - 1)
print(f"\nAverage score: {average:.2f}")