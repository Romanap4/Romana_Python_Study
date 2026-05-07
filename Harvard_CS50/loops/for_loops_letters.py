# def main():
#     print(write_letter("Mario", "Princess Peach"))
#     print(write_letter("Luigi", "Princess Peach"))
#     print(write_letter("Daisy", "Princess Peach"))
#     print(write_letter("Yoshi", "Princess Peach"))

# def write_letter(receiver, sender):
#     return f"""
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#        Dear {receiver}

#        You are cordially invited to a ball at 
#        Peach's Castle this evening, 7:00 PM.
    
#        Sincerely,
#        {sender}
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#     """

# main()

# This program can have a better design using for loops:

def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    # for i in range(len(names)):
    #     print(write_letter(names[i], "Princess Peach"))
    
# A feature of Python is that any kind of list can be iterated over directly:

    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver}

       You are cordially invited to a ball at 
       Peach's Castle this evening, 7:00 PM.
    
       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()
