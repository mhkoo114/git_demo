# open(name, mode, encoding)
# name - target file (python.txt)
# mode - open mode of file (read-only, write, add, ...)
# encoding - cipher type (UTF-8, ...)

# if using '\' will error, use '/' , or 'r' prefix, or '\\' instead
f = open("C:/develop/workplace/codeTwo/python/tests/Test.txt", "r", encoding="UTF-8")
print(type(f))

# # read according num of read param
# # if not giving param, will read all content
# print(f.read())
# # read all the content in the file
# content = f.readlines()
# # if invoke 2 read func continuously, it will continue from the previous point it left
# # in the next line, it will print nothing, becuz ady finish reading
# print(content)

# # readline() will read line-by-line
# line1 = f.readline()
# line2 = f.readline()
# print(line1,line2)

# use a for loop to read obj f
for line in f:
    print(line, end=" ")

# close()
# if not closing, the file will keep occupied by python
f.close()

# a small divider
import time
time.sleep(5)

# with open, the file will close automatically after use
with open("C:/develop/workplace/codeTwo/python/tests/Test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)