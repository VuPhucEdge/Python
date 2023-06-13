def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


user_prompt = "Type add, show, edit or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # slicing
        todo = user_action[4:]

        todo = input('Enter a todo: ')+'\n'

        todos = get_todos()

        todos.append(todo+'\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(input("Number of the todo to edit: "))

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number-1] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(input("Number of the todo to complete: "))

            todos = get_todos()

            todos.pop(number-1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Hey, you entered an unknown command')

print('Bye!')
