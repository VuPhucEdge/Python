user_prompt = "Type add, show, edit or exit: "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')+'\n'

            fo = open('todos.txt', 'r')
            todos = fo.readline()
            fo.close()

            todos.append(todo)

            fo = open('todos.txt', 'w')
            fo.writelines(todos)
            fo.close()
        case 'show':
            fo = open('todos.txt', 'r')
            todos = fo.readline()
            fo.close()

            for index, item in enumerate(todos):
                item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number-1] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command')

print('Bye!')
