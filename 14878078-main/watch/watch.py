import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        matches = re.search(r"(http)(s)?:\/\/(www\.)?youtube\.com\/embed\/(\w+)", s)
        if matches:
            id = matches.group(4)
            return f"https://youtu.be/{id}"


...


if __name__ == "__main__":
    main()