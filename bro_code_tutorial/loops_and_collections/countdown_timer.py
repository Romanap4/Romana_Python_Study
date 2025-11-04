import time
# importing the time module
# SLEEP FUNCTION --> the program sleeps for a given amount of seconds
# to countdown in reverse, you can enclose the range function within the reversed function or use a -1 step

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

# % 24 was not necessary since there are no days in the timer
