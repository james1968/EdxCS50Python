math_input = input("Enter your sum: ")
math_lst = math_input.split(" ")

match math_lst[1]:
    case '+':
        ans = float(math_lst[0]) + float(math_lst[2])
        print(f"{ans:.1f}")
    case '-':
        ans = float(math_lst[0]) - float(math_lst[2])
        print(f"{ans:.1f}")
    case '*':
        ans = float(math_lst[0]) * float(math_lst[2])
        print(f"{ans:.1f}")
    case '/':
        ans = float(math_lst[0]) / float(math_lst[2])
        print(f"{ans:.1f}")
