def main():
    x = get_fraction("What's the fraction of petrol ")
    if 99 <= x < 101:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print(f"{x}%")

def get_fraction(prompt):
    while True:
        fraction = input(prompt)
        try:
            num, den = fraction.split('/')
            fraction = round(int(num)/int(den) * 100)
            if fraction > 100:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return fraction

main()