def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if length(s) and start_letters(s) and spaces_check(s) and check_numbers(s) and check_zero(s):
        return True
    else:
        return False

def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def start_letters(s):
    if length(s):
        if s[0].isalpha and s[1].isalpha():
           return True
        else:
            return False

def spaces_check(s):
    punctuation = [' ', '.', '!', '?', ',']
    for letter in s:
        if letter in punctuation:
            return False
    return True

def check_numbers(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, len(s)-1):
        if s[i] in numbers and s[i+1].isalpha():
            return False
    return True

def check_zero(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, len(s)-1):
        if s[i] == '0' and s[i+1] in numbers:
            return False
    return True

if __name__ == "__main__":
    main()