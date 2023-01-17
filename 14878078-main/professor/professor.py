import random


def main():
    level = get_level()
    count = 1
    score = 0
    for i in range(0, 10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        real_ans = num1 + num2
        ans = input(f"{num1} + {num2} = ")
        try:
            int(ans)
        except ValueError:
            print("EEE")
            count += 1

        while int(ans) != num1 + num2:
            print("EEE")
            ans = input(f"{num1} + {num2} = ")
            try:
                int(ans)
            except ValueError:
                print("EEE")
                count += 1
            count += 1
            if count == 3:
                print(f"{num1} + {num2} = {real_ans}")
                break

        if int(ans) == num1 + num2:
            score += 1
    print(score)



def get_level():
    while True:
        level = input("Level: ")
        try:
            int(level)
            if 1 <= int(level) <=3:
                return int(level)
            else:
                True
        except ValueError:
            level = input("Level: ")


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
        return number
    elif level == 2:
        number = random.randint(10, 99)
        return number
    else:
        number = random.randint(100, 999)
        return number




if __name__ == "__main__":
    main()