import sys
from PIL import Image, ImageOps
import os

def main():
    validation()
    image_overlay()

def validation():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

    try:
        open(file1)

    except FileNotFoundError:
        print(f"Input does not exist")
        sys.exit(1)

    valid_ext = [".jpeg", ".jpg", ".png"]

    file1_ext = os.path.splitext(file1)
    file2_ext = os.path.splitext(file2)

    if file1_ext[1].lower() not in valid_ext:
        print(file1_ext)
        print("Invalid file")

    elif file2_ext[1].lower() not in valid_ext:
        print("Invalid output")

    elif file1_ext[1] != file2_ext[1]:
        print("Input and output have different extensions")
        sys.exit(1)


def image_overlay():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    shirt = Image.open("shirt.png")
    shirt_size = (shirt.size)
    before = Image.open(file1)
    before_resize = ImageOps.fit(before, shirt_size, bleed=0.0, centering=(0.5, 0.5))
    before_resize.paste(shirt, shirt)
    before_resize.save(file2)


if __name__ == "__main__":
    main()