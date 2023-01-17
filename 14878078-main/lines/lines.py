import sys

def main():
    counter()

def counter():
    if len(sys.argv) > 2:
        print("Too many command line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command line arguments")
        sys.exit(1)

    py_file = sys.argv[1]
    count = 0

    if py_file[-3:] != ".py":
        print("Not a python file")
        sys.exit(1)

    try:
        with open(py_file) as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    pass
                elif line.isspace():
                    pass
                else:
                    count += 1
        print(count)
        return count

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

if __name__ == "__main__":
    main()
