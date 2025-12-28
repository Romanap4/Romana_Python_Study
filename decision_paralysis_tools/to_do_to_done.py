# chores and tasks input

import random

to_do_list = []
task = 0

def create_to_do_list():
    
    adding_tasks = True
    while adding_tasks:
        task = input("Add a task or a chore to your to do list (q to quit): ").lower()
        to_do_list.append(task)
        if task == "q":
            adding_tasks = False

    to_do_list.remove("q")

    print()
    print(" +++ Your to do list was succesfully created! +++ ")
    print()

    for task in to_do_list:
        print(f"[ ] {task}")

    print()
    print(" +++ You got this! Go get'em! +++ ")
    print()

# task selection

chosen_task = 0
done_list = []

def task_selection():
    chosen_task = random.choice(to_do_list)

    print(f"Your next task is: {chosen_task}")
    print()
    print(" +++ You can do this! +++ ")
    print()

    done_list.append(chosen_task)
    to_do_list.remove(chosen_task)

# this feels like cheating xD

def create_done_list():
    
    for chosen_task in done_list:
        print(f"[✓] {chosen_task}")

def main():
    create_to_do_list()
    task_selection()
    create_done_list()
    
    unfinished_tasks = input("Would you like another task? (y/n): ").lower()

    while unfinished_tasks == "y":
        task_selection()
        create_done_list()

        print()
        print(" +++ Well done! I'm so proud of you! +++ ")
        print()

        unfinished_tasks = input("Would you like another task? (y/n): ").lower()

        if unfinished_tasks == "n" or to_do_list == []:
            break
        else:
            print("Please enter y or n!")

    print()
    print(" +++ Well done! I'm so proud of you! +++ ")
    print()

if __name__ == '__main__':
    main()
