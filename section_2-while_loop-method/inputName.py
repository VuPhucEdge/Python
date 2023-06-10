user_name = "What is your name? "

names = []

while True:
    name = input(user_name)
    name = name.capitalize()
    names.append(name)
    print(name)
