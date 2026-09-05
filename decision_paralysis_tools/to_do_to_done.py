# chores and tasks input

import random
import dice_ascii_art

to_do_list = []
task = 0

# ask the user how many tasks they want to enter and use that for while loop repetiton

def create_to_do_list():
    
    adding_tasks = True
    while adding_tasks:
        task = input("Add a task or a chore to your to do list (q to quit): ").lower().strip()
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

def award_points():
    pass

def main():
    create_to_do_list()

    # this is the outer loop

    while to_do_list:
        task_selection()
        create_done_list()

        print()
        print(" +++ Well done! I'm so proud of you! +++ ")
        print()

        # this is the inner loop

        while True:
            unfinished_tasks = input("Would you like a different task (y/n)?: ").lower().strip()
            if unfinished_tasks in ("y", "n"):
                break
            print("Please enter y or n!")

        if unfinished_tasks == "n":
                break

    print()
    print(" +++ All done or you chose to stop. Great job! +++ ")
    print()
    

if __name__ == '__main__':
    main()
