from sys import argv
script, user_name = argv
prompt = f"{script}>>>>"

print(f"Hi {user_name}, I'm the {script}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt + f"{user_name}")

print(f"What kind of computer do you have?")
computer = input(prompt)


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.
And you have a {computer} computer. Nice.
""")
