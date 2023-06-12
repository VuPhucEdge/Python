user_prompt = "Type add, show, edit or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        # slicing
        todo = user_action[4:]

        todo = input('Enter a todo: ')+'\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number-1] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number-1)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'exit' in user_action:
        break
    else:
        print('Hey, you entered an unknown command')

print('Bye!')

# dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
