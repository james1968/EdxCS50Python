from datetime import date
import re
import sys
import inflect
import re
p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    if validate(birth_date):
        year, month, day = birth_date.split("-")
        birth_d = date(int(year), int(month), int(day))
        today = date.today()
        #today = date(2000,1,1)
        day_diff = (today - birth_d)
        total_days = day_diff.days
        mins = total_days * 24 * 60
        ans = p.number_to_words(mins, andword="").capitalize() + " minutes"
        #ans2 = re.sub(r' and', '', ans)
        print(ans)

def validate(b):
    matches = re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", b)

    if matches:
        if int(matches.group(1)) > 2022:
            sys.exit("Invalid date")
        elif int(matches.group(2)) > 12:
            sys.exit("Invalid date")
        elif int(matches.group(3)) > 31:
            sys.exit("Invalid date")
        else:
            return True
    else:
        sys.exit("Invalid date")


def get_days(b):
    year, month, day = b.split("-")
    birth_d = date(int(year), int(month), int(day))
    today = date.today()
    #today = date(2000,1,1)
    day_diff = (today - birth_d)
    total_days = day_diff.days
    mins = total_days * 24 * 60
    ans = num2words(mins).capitalize() + " minutes"
    ans2 = re.sub(r' and', '', ans)
    return ans2


if __name__ == "__main__":
    main()