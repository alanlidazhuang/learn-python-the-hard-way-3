from sys import argv

script, input_file = argv

def print_all(f):            #注意这里f是个变量
    print(f.read())

def rewind(f):
    f.seek(0)                 #seek用法参考https://blog.csdn.net/qq_42514453/article/details/84900411

def print_a_line(line_count, f):
    print(line_count, f.readline())   #f.readline()读取整行的文本内容

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print thress lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


  
