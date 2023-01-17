def main():
    time = input("Enter time in 24 hour format: ")
    meal_time = convert(time)
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    if "a.m." in time:
        am_time = time.strip(" a.m.")
        hours, minutes = am_time.split(":")
    elif "p.m." in time:
        pm_time = time.strip(" p.m.")
        hours, minutes = pm_time.split(":")
        if float(hours) > 12:
            hours = float(hours) + 12
    else:
        hours, minutes = time.split(":")

    min_dec = float(minutes) / 60
    total_time = float(hours) + min_dec
    return total_time



if __name__ == "__main__":
    main()