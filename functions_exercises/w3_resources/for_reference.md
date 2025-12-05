def ask_name():
    return input("Enter your name: ")

# Look, I'll remove the return statement again
# None, see? Why's that, because the first input is running, is trying to store the data what we are typing, but it is not returning to be stored, that's why it's resulting in "None"
# Now if you add the Return statement

# Got it? I think so, but leave all the comments, I need to do it a few times
# Let me help you...

'''
[ask_name]  
   │  
   ▼  
[return input]                → prompts for and returns user input  
   │  
   ▼  
[input receives data]         → captures the value entered by the user  
   │  
   ▼  
[This_Could_be_ANYTHING]      → stores the received input in a variable  
   │  
   ▼  
[welcome_message(This_Could_be_ANYTHING)]      → passes variable as an argument to another function  
   │  
   ▼  
[string interpolation]        → uses argument as placeholder in a message/output

Does this make sense now? Aight, let's call it a day then
'''
    
def welcome_message(name):
    print(f"Welcome to the group, {name}!")

This_Could_be_ANYTHING = ask_name()
message = welcome_message(This_Could_be_ANYTHING)
