import sys
import csv

def main():
    validation()
    convert()

def validation():
    if len(sys.argv) > 3:
        print("Too many command line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command line arguments")
        sys.exit(1)
    elif len(sys.argv) == 3:
        file1 = sys.argv[1]

    try:
        open(file1)

    except FileNotFoundError:
        print(f"Could not read {file1}")
        sys.exit(1)


def convert():
    new_file = []
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    with open(file1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_file.append({"first": row["name"].split(",")[1].lstrip(), "last": row["name"].split(",")[0], "house": row["house"]})

    with open(file2, "w") as file:
        writer = csv.DictWriter(file,  fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in new_file:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()
