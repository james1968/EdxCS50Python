def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip()
    greet_list = greeting.split(",")
    if greet_list[0].lower() == "hello":
        return 0
    elif greet_list[0][0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
