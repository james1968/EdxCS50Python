def convert(entry):
    entry_lst = entry.split()
    ans_str = ""
    for i in entry_lst:
        if i == ":)":
            ans_str += " " + "\U0001F642" + " "
        elif i == ":(":
            ans_str += " " + "\U0001F641" + " "
        else:
            ans_str += i
    ans_str = ans_str.strip(" ")
    print(ans_str)

def main():
     entry = input()
     convert(entry)

if __name__ == '__main__':
    main()

