def view_todos(todos):
    if not todos:
        return "No todos found."
    lines = [f"{i+1}. [{'x' if t['done'] else ' '}] {t['desc']}" for i, t in enumerate(todos)]
    return "\n".join(lines)

def create_todo(todos, description):
    todos.append({"desc": description, "done": False})
    return todos

def update_todo(todos, index, new_desc=None, new_done=None):
    if index < 1 or index > len(todos):
        raise IndexError("Invalid todo number.")
    if new_desc is not None:
        todos[index-1]['desc'] = new_desc
    if new_done is not None:
        todos[index-1]['done'] = new_done
    return todos

def delete_todo(todos, index):
    if index < 1 or index > len(todos):
        raise IndexError("Invalid todo number.")
    todos.pop(index-1)
    return todos
