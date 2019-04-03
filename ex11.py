print("How old are you?", end ='')   #加' '的目的是How old are you?这一行不会结束，输入的数字会在这句话之后，而不是另起一行
age = int(input())   # 限制输入年龄的字符类型
print(">>>>>>> age=", repr(age))
print("How tall are you?")
height = input()
print("How much do you weight?", end ='') 
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")