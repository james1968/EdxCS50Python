def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    cost = d[1:]
    print(cost)
    return float(cost)

def percent_to_float(p):
    percent = p[:-1]
    return float(float(percent) / 100)

main()