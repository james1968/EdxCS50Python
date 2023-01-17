import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if matches:
        if int(matches.group(1)) > 255:
            return False
        if int(matches.group(2)) > 255:
            return False
        if int(matches.group(3)) > 255:
            return False
        if int(matches.group(4)) > 255:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()