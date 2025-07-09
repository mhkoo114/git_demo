arr = [
    [[1, 2, 3], [2, 3, 4], [3, 5, 2]],
    [[3, 4, 2], [7, 5, 9], [8, 4, 1]],
    [[9, 2, 1], [5, 3, 7], [8, 9, 6]]
]
# to traverse using nested loop
for a in arr:
    for b in a:
        for c in b:
            print(c, end="")