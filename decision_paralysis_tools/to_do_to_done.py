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
    print("++++++++++++++++++++++++++++++++++++++++")
    print("Your to do list was succesfully created!")
    print("++++++++++++++++++++++++++++++++++++++++")
    print()

    for task in to_do_list:
        print(f"[] {task}")

    print()
    print("++++++++++++++++++++++++++++++++++++++++")
    print("        You got this! Go get'em!        ")
    print("++++++++++++++++++++++++++++++++++++++++")
    print()

create_to_do_list()

# task selection

chosen_task = 0 # OMYGOD THIS IS WHY IT WAS SHOWING ZERO!

def task_selection():
    chosen_task = random.choice(to_do_list)

    print(f"Your next task is: {chosen_task}")
    print()
    print("++++++++++++++++++++++++++++++++++++++++")
    print("            You can do this!            ")
    print("++++++++++++++++++++++++++++++++++++++++")
    print()

task_selection()

# migration of tasks to the done list

# this would become function 3
done_list = []

def create_done_list(chosen_task):
    
    done_list.append(chosen_task)
    
    for chosen_task in done_list:
        print(f"[✓] {chosen_task}")

create_done_list(chosen_task)

# UAAAAARGH HERE WE GO WITH THE VARIABLE SCOPE AGAIN LMAO T_T
# OKAY WE NEED FUNCTIONS? Which means I'll have to tackle this variable scope issue after all
# VISION:
# function 1, 2, 3, call order: 1, 2, 3, 2, 3, 2, 3, 2, 3 --> I wanna do this and repeat it as many times as there are tasks
# THERE WE GO WITH THE SQUIGGLY LINE BECAUSE OF VARIABLE SCOPE YAY 
# come on Mana, you can do this, you need to learn this sooner or later
# how do I "export" the chosen_task variable back to global after it was assigned a random value? 
