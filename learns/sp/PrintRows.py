# increment multiply table
"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print(f"{col} * {row} = {col*row}",end="\t")
        col+=1
    print("")
    row+=1
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()