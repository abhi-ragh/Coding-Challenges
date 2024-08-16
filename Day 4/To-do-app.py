"""
Author: Abhiragh
Date: 16/08/2024
Description: Simple Terminal Based To-Do App
"""

tasks = []

def add():
    task = {}
    task["desc"] = input("Enter Task Description: ")
    task["done"] = False
    tasks.append(task)

def view():
    print("\nTasks")
    for task in tasks:
        task_status = f" {tasks.index(task)+1}. {task['desc']} "
        print(task_status, ": Incomplete") if task["done"] == False else print(task_status, ": Completed")
    print("\n")

def mark():
    view()
    choice = int(input("Enter Task to Mark as Completed: "))
    tasks[choice-1]["done"] = True

def delete():
    view()
    choice = int(input("Enter Task to Delete: "))
    tasks.remove(tasks[choice-1])


print("\n1. Add Task\n2. View Tasks\n3. Mark Complete\n4. Delete Task\n5. Exit")
while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        mark()
    elif choice == 4:
        delete()
    elif choice == 5:
        break
    else:
        print("\nInvalid Choice")

