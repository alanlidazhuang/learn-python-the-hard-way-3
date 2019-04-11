from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")

print(txt.read())                      #只能对变量做read()操作

print("Type the file again:")
file_again = input(">>>")
txt_again = open(file_again)

print(txt_again.read())

print("hello")

