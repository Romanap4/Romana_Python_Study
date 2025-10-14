import time                          # importing time module

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):       # to countdown in reverse, you can enclose the range function within the reversed function
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)             # % 24 was not necessary since there are no days in the timer
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)                     # program sleeps for a given amount of seconds

print("TIME'S UP!")
