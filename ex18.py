#自定义函数

def print_two(*args):
    arg1, arg2 = args       #注意自定义函数定义的语句前有缩进
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I GOT nothing.")
    print("\n")
    print(" I GOT it.")



print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()




