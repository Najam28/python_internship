from function import view_todos, create_todo, update_todo, delete_todo

def main():
    print("=== Todo List CRUD CLI (In-Memory) ===")
    todos = []

    while True:
        print("\nMenu:")
        print("1. View Todos")
        print("2. Create Todo")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                print("\nTodos:")
                print(view_todos(todos))

            elif choice == "2":
                desc = input("Enter new todo description: ").strip()
                if not desc:
                    print("Description cannot be empty.")
                    continue
                todos = create_todo(todos, desc)
                print("Todo created.")

            elif choice == "3":
                print("\nCurrent Todos:")
                print(view_todos(todos))
                if not todos:
                    continue
                idx = input("Enter todo number to update: ").strip()
                if not idx.isdigit():
                    print("Please enter a valid number.")
                    continue
                idx = int(idx)
                new_desc = input("Enter new description (leave blank to keep current): ").strip()
                new_done_input = input("Is this todo done? (y/n/leave blank to keep current): ").strip().lower()
                new_done = None
                if new_done_input == 'y':
                    new_done = True
                elif new_done_input == 'n':
                    new_done = False
                todos = update_todo(todos, idx, new_desc if new_desc else None, new_done)
                print("Todo updated.")

            elif choice == "4":
                print("\nCurrent Todos:")
                print(view_todos(todos))
                if not todos:
                    continue
                idx = input("Enter todo number to delete: ").strip()
                if not idx.isdigit():
                    print("Please enter a valid number.")
                    continue
                todos = delete_todo(todos, int(idx))
                print("Todo deleted.")

            elif choice == "5":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1-5.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
