import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = sys.argv[2]
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

try:
    figlet.setFont(font=f)
except:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))