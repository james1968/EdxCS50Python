import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M)$", s)
    if matches:
        elements = matches.groups()
        if int(elements[1]) > 12 or int(elements[5]) > 12:
            raise ValueError
        am_time = convert_hours_mins(elements[1], elements[2], elements[3])
        pm_time = convert_hours_mins(elements[5], elements[6], elements[7])
        return am_time + " to " + pm_time
    else:
        raise ValueError

def convert_hours_mins(hour, mins, am_or_pm):
    if am_or_pm == "PM":
        if int(hour) == 12:
            new_hours = 12
        else:
            new_hours = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hours = 0
        else:
            new_hours = int(hour)

    if mins == None:
        new_mins = ":00"
        new_time = f"{new_hours:02}" + new_mins
    else:
        new_time = f"{new_hours:02}" + ":" + mins

    return new_time


if __name__ == "__main__":
    main()