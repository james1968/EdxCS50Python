import sys
import csv
from tabulate import tabulate

def main():
    check_arg()

def check_arg():
    if len(sys.argv) > 2:
        print("Too many command line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command line arguments")
        sys.exit(1)

    menu = sys.argv[1]
    menu_list = []

    if menu[-4:] != ".csv":
        print("Not a csv file")
        sys.exit(1)

    with open(menu) as file:
        reader = csv.reader(file)
        for row in reader:
            menu_list.append([row[0], row[1], row[2]])
        print(tabulate(menu_list, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()