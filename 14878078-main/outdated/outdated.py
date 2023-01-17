def main():
    outdated()



def outdated():
    months = [
    "None",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

    while True:
        date_list = []
        date = input("Date: ").strip()

        if date.split(" ")[0] in months:
            date_list = date.split(" ")
            if months.index(date_list[0]) > 12 or int(date_list[1].rstrip(',')) > 31:
                pass
            elif date_list[1][-1] != ",":
                pass
            else:
                print(f"{date_list[2]}-{str(months.index(date_list[0])).rjust(2, '0')}-{date_list[1].rstrip(',').rjust(2, '0')}")
                break
        try:
            int(date.split("/")[0])
            date_list = date.split("/")
            if int(date_list[0]) > 12 or int(date_list[1]) > 31:
                pass
            else:
                print(f"{date_list[2]}-{date_list[0].rjust(2, '0')}-{date_list[1].rjust(2, '0')}")
                break
        except ValueError:
            pass


main()