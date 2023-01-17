import random
import string
import os.path


def main():

    inc_numbers = input("Do you want your password to include numbers: ").lower()
    inc_special_chars = input("Do you want your password to include special characters: ").lower()
    pw_length = int(input("How long do you want your password to be: "))
    list_letters = list(string.ascii_letters)

    if inc_numbers == "yes":
        list_letters = numbers(list_letters)

    if inc_special_chars == "yes":
        list_letters = special_chars(list_letters)
    print(list_letters)

    pw = create_pw(pw_length, list_letters)

    write = input("Do you want to write the details to file: ").lower()

    if write == "yes":
        file_name = input("Filename to store your new password: ")
        account = input("Account password is for: ")
        write_pw(account, file_name, pw)
        print(pw)
    else:
        print(pw)

def numbers(list_letters):
    for i in range(0, 10):
        list_letters.append(str(i))
    else:
        pass

    return list_letters


def special_chars(list_letters):
    special_chars_list = ["!", "@", "£", "$", "%", "&", "?", "#", "^", "•", "_", "-"]
    for i in special_chars_list:
        list_letters.append(i)
    else:
        pass

    return list_letters


def create_pw(pw_length, list_letters):
    pw = ""
    for i in range(1, pw_length+1):
       pw += random.choice(list_letters)

    return pw


def write_pw(account, file_name, pw):
    if os.path.exists(f"{file_name}.txt"):
        f = open(f"{file_name}.txt", 'a')
        f.write(f"\nAccount: {account}, Password: {pw}")
    else:
        with open(f'{file_name}.txt', 'w') as f:
            f.write(f"Account: {account}, Password: {pw}")

if __name__ == "__main__":
    main()