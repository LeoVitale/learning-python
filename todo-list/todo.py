from typing import TypedDict


class Task(TypedDict):
    name: str
    completed: bool


def add_task(tasks: list[Task], task_name: str = "Generic task") -> None:
    task: Task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"\nTask '{task_name}' added!")


def list_tasks(tasks: list[Task]) -> None:
    print("\nTasks:")
    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. {task['name']} - {'Completed' if task['completed'] else 'Pending'}"
        )


def update_task(tasks: list[Task], task_index: int, new_task_name: str) -> None:
    if task_index < 0 or task_index >= len(tasks):
        print("\nInvalid task number!")
        return
    tasks[task_index]["name"] = new_task_name
    print(f"\nTask '{new_task_name}' updated!")


def complete_task(tasks: list[Task], task_index: int) -> None:
    tasks[task_index]["completed"] = True
    print("\nTask completed!")


def delete_completed_tasks(tasks: list[Task]) -> None:
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)

    print("\nCompleted tasks deleted!")


tasks: list[Task] = []


while True:
    print("\nTask Manager Menu")
    print("1. Add task")
    print("2. List tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Exit")

    option = input("Enter the desired option: ")

    if option == "1":
        new_task_name = input("Enter the task name: ")
        add_task(tasks, new_task_name)
        print(tasks)
    elif option == "2":
        list_tasks(tasks)
    elif option == "3":
        list_tasks(tasks)
        task_index = int(input("Enter the task number to update: ")) - 1
        task_name = input("Enter the new task name: ")
        update_task(tasks, task_index, task_name)
    elif option == "4":
        list_tasks(tasks)
        task_index = int(input("Enter the task number to complete: ")) - 1
        complete_task(tasks, task_index)
    elif option == "5":
        delete_completed_tasks(tasks)
    elif option == "6":
        break

print("Goodbye!")
