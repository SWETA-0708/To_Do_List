# file:todo_list.py
def display_menu():
    print("\n====To-do List Menu====")
    print("1.add Task")
    print("2.View Tasks")
    print("3.Mark Task as Done")
    print("4.Exit")

def add_task(tasks,task):
    tasks.append(task)
    print(f'Task"{task}"added successfully!')

def view_task(tasks):
    if not tasks:
        print("No tasks in the to-do list")
    else:
        print("\n=== To-Do List ===")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}.{task}")
def mark_task_as_done(tasks,index):
    if 1<= index <= len(tasks):
        done_task = tasks.pop(index-1)
        print(f'Task"{done_task}"marked as done and removed from the list.')
    else:
        print("Invalid task index")

def main():
    tasks=[]

    while True:
        display_menu()
        choice=input("Enter your choice(1-4):")

        if choice=='1':
            task=input("enter the task:")
            add_task(tasks,task)
        elif choice == '2':
            view_task(tasks)
        elif choice=='3':
            view_task(tasks)
            index=int(input("enter the task index to mark as done:"))
            mark_task_as_done(tasks,index)
        elif choice=='4':
            print("exiting the to-do list application.Goodbye!")
            break
        else:
            print("Invalid choice.Please enter a number between 1 and 4")
if __name__=="__main__":
 main()
