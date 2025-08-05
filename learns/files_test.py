# count a word appear how many time in a file
f = open("C:/develop/workplace/codeTwo/python/tests/Test.txt", "r", encoding="UTF-8")
count = 0
for line in f:
    if "is" in line:
        count+=1
print(count)
f.close()