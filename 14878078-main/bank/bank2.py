greeting = input("Greeting: ")
greeting = greeting.strip()
greet_list = greeting.split(",")
print(greet_list[0].lower())
if greet_list[0].lower() == "hello":
    print("$0")
elif greet_list[0][0].lower() == "h":
    print("$20")
else:
    print("$100")

