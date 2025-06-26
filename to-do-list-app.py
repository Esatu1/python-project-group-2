
# 3 To-Do List App (Text-Based)

# Build a to-do list manager that:
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list, delete tasks by number, and mark tasks as complete.
# Keeps looping until the user types “exit”.
# Shows a summary at the end: number of completed tasks vs pending.
# Skills practiced: lists, string parsing, loops, input, CRUD basics

# Initialize the to-do list
todo_list = []

print("Welcome to the To-Do List Manager!")
print("Type commands to manage your tasks. Available commands:")
print("add <task description> - <priority> (e.g., add Buy eggs - high)")
print("view → View all tasks")
print("delete <task number> → Delete a task")
print("complete <task number> → Mark a task as complete")
print("exit → Exit the app and view summary\n")

# Start main loop
while True:
    command = input("Enter command: ").strip().lower()

    if command == "exit":
        break

    elif command.startswith("add "):
        try:
            # Extract task and priority
            raw = command[4:]  # Remove "add " part
            task_text, priority = raw.split(" - ")
            task = {
                "description": task_text.strip().capitalize(),
                "priority": priority.strip().lower(),
                "completed": False
            }
            todo_list.append(task)
            print("Task added.\n")
        except ValueError:
            print("Use format: add Task Description - priority\n")

    elif command == "view":
        if not todo_list:
            print("Your to-do list is empty.\n")
        else:
            print("\n Your To-Do List:")
            for idx, task in enumerate(todo_list, 1):
                status = "Done" if task["completed"] else "❗Pending"
                print(f"{idx}. {task['description']} [{task['priority']}] - {status}")
            print()

    elif command.startswith("delete "):
        try:
            index = int(command.split()[1]) - 1
            if 0 <= index < len(todo_list):
                removed = todo_list.pop(index)
                print(f"Removed: {removed['description']}\n")
            else:
                print("Invalid task number.\n")
        except:
            print("Use format: delete <task number>\n")

    elif command.startswith("complete "):
        try:
            index = int(command.split()[1]) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["completed"] = True
                print(f"Marked as complete: {todo_list[index]['description']}\n")
            else:
                print("Invalid task number.\n")
        except:
            print("Use format: complete <task number>\n")

    else:
        print("Unknown command. Try again.\n")

# === Summary at Exit ===
completed = sum(1 for t in todo_list if t["completed"])
pending = len(todo_list) - completed

print("\n To-Do List Summary")
print(f"Completed Tasks: {completed}")
print(f"Pending Tasks: {pending}")
print("Goodbye! See you next time!\n")
