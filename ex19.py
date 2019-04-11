def cheese_and_crackers(cheese_count, boxes_of_crackers):     #注意别落冒号
    print(">>>>>cheese_count =", cheese_count, "; boxes_of_crackers =", boxes_of_crackers)     #格式化输出形式
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party.")
    print("Get a blanket.\n")                                  #转移符号能表达，这里既是空一行
    print("<<<<<<exit cheese_and_crackers")


print("We can just give the fuction numbers dirextly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("In addtion, we can use input variables:")
amount_of_cheese_input = input("cheese~~~~~")
amount_of_crackers_input = input("crackers~~~~~")

cheese_and_crackers(amount_of_cheese_input, amount_of_crackers_input)


print("We can even do math inside too:")
cheese_and_crackers(66+55, 87-89)


print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 999, amount_of_crackers - 123)

