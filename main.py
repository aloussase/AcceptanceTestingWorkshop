todos = dict()
todo_id = 0

def add_todo(todo):
    global todo_id
    todos[todo_id] = { "id": todo_id, "text": todo, "completed": False }
    todo_id += 1


def list_todos():
    return todos


def mark_complete(todo_id):
    todos[todo_id]['completed'] = True


def reverse_todo(todo_id):
    todos[todo_id]['text'] = todos[todo_id]['text'][::-1]


if __name__ == "__main__":
    print("a) Add todo, b) List todos, c) Mark todo complete, d) Reverse todo")

    while True:
        action = input("action> ")
        match action:
            case "a":
                todo = input("Enter todo: ")
                add_todo({"text": todo, "complete": False})
            case "b":
                list_todos()
            case "c":
                todo_id = int(input("Enter todo id: "))
                mark_complete(todo_id)
            case "d":
                todo_id = int(input("Enter todo id: "))
                reverse_todo(todo_id)
            case _:
                break
