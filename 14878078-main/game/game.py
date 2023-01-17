import random

level = input("Level: ")
while True:
    if level.isalpha():
        level = input("Level: ")
    elif int(level) <= 0:
        level = input("Level: ")
    else:
        number = random.randint(1, int(level))
        print(number)
        break

guess = input("Guess: ")
while True:
    if guess.isalpha():
        guess = input("Guess: ")
    elif int(guess) < 0:
        guess = input("Guess: ")
    elif int(guess) < number:
        print("Too small!")
        guess = input("Guess: ")
    elif int(guess) > number:
        print("Too large!")
        guess = input("Guess: ")
    elif int(guess) == number:
        print("Just right!")
        break
    else:
        guess = input("Guess: ")
