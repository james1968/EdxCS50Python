name = input("Enter name to convert: ")

name_lst = "".join([(" "+i if i.isupper() else i) for i in name]).strip().split()

new_lst = []
for word in name_lst:
    new_word = ""
    for j in range(0, len(word)):
        new_word += word[j].lower()
    new_lst.append(new_word)

print("_".join(new_lst))