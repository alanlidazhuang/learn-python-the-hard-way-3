from sys import argv

script, filename = argv

print(f"Before erasing {filename}, We're going to print it first.")

target_before = open(filename)  #注意这里没有'w'，有'w'会报错
print(target_before.read())

target_before.close()

print(f"We're going to erase {filename}.")

input("??????")

print("Opening the file......")
target_after = open(filename, 'w')    #'w'

print("Erasing the file...Goodbye!")

target_after.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

target_after.write(line1)
target_after.write("\n")
target_after.write(line2)
target_after.write("\n")
target_after.write(line3)
target_after.write("\n")

print("And finally, we close it.")
target_after.close()



