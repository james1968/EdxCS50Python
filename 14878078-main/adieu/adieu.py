import inflect
import sys

p = inflect.engine()

names = []
response = "Adieu, adieu, to "

while True:
    try:
        name = input("Name: ")
        names.append(name)
        ans = response + p.join(names)

    except EOFError:
        print(ans)
        sys.exit()