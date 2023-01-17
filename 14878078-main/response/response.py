from validator_collection import validators, checkers, errors


def main():

    print(validate(input("Email: ")))


def validate(email):

    try:
        e = validators.email(email)

    except errors.EmptyValueError:
        return "Invalid"

    except errors.InvalidEmailError:
        return "Invalid"

    if checkers.is_email(e):
        return "Valid"


if __name__ == "__main__":
    main()

