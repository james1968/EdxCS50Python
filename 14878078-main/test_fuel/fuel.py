def main():
    fraction = input("Fraction: ")
    fraction_conv = convert(fraction)
    print(type(fraction_conv))
    print(gauge(fraction_conv))

def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            new_num = int(num)
            new_den = int(den)
            frac = new_num / new_den
            if frac <= 1:
                perc = int(frac * 100)
                return perc
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if 99 <= percentage < 101:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()