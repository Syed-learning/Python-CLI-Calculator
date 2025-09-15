# simple_todo.py

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                tasks.pop(num - 1)
                save_tasks(tasks)
            except:
                print("Invalid number.")
        elif choice == "4":
            print("THANK YOU")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
