# Implement a program that prompts the user for a time and outputs whether it's `breakfast time`, `lunch time`, or `dinner time`. If it's not time for a meal, don't output anything at all. Assume that the user's input will be formatted in 24-hour time as `#:##` or `##:##`. And assume that each meal's time range is inclusive. For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime in between, it's time for breakfast.

# Breakfast between 7:00 and 8:00
# Lunch between 12:00 and 13:00
# Dinner between 18:00 and 19:00

# Structure your program wherein `convert` is a function (that can be called by `main`) that converts `time`, a `str` in 24-hour format, to the corresponding number of hours as a `float`. For instance, given a `time` like `"7:30"` (i.e., 7 hours and 30 minutes), `convert` should return `7,5` (i.e., 7,5 hours).

time = input("What time is it? ")

def main(time):
    time = convert(time)
    if time >= 7 and time <=8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print()

def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) * 60 + float(minutes)
    return time / 60

if __name__ == '__main__':
    main(time)
