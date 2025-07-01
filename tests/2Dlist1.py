"""
data = [
    ["Name", "Age"],
    ["Alice", 20],
    ["Bob", 22]
]
for row in data:
    for item in row:
        print(item, end="\t")
    print()

###########################################
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1]) # row 0, column 1

# nested loop for traverse
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# use index access the list
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()