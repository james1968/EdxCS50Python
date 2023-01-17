from collections import Counter

def main():
    list()

def list():
    g_dict = {}
    g_list = []
    while True:
        try:
            item = input()
            g_list.append(item)
        except EOFError:
            print("\n")
            break
    g_list.sort()
    for i in g_list:
        g_dict[i] = g_dict.get(i, 0) + 1

    for key, value in g_dict.items():
        print(f"{value} {key.upper()}")


main()