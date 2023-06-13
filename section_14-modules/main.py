from functions import get_todos, write_todos

user_prompt = "Type add, show, edit or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # slicing
        todo = user_action[4:]

        todo = input('Enter a todo: ')+'\n'

        todos = get_todos('todos.txt')

        todos.append(todo+'\n')

        write_todos('todos.txt', todos)
    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(input("Number of the todo to edit: "))

            todos = get_todos('todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number-1] = new_todo + '\n'

            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(input("Number of the todo to complete: "))

            todos = get_todos()

            todos.pop(number-1)

            write_todos('todos.txt', todos)
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Hey, you entered an unknown command')

print('Bye!')
