from sys import argv

from os.path import exists

script, from_file, to_file = argv      #注意，“from_file”和“to_file”是文件名

print(f"Copying from {from_file} to {to_file}.")


in_file = open(from_file)             #注意，“in_file”是变量名
print(">>>>>>>", repr(in_file))
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Dose the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")

input(">>>>>")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

 #经过测试，发现，这里写入“write”是将被写入文件中内容覆盖，即原有“txt17_to.txt”中内容会被抹掉
 

