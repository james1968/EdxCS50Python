print("Amount Due: 50")
coin = int(input("Insert Coin: "))
amount = 50

while True:
    if coin == 25 or coin == 10 or coin == 5:
        amount = amount - coin
        if amount < 1:
           print(f"Change Owed: {abs(amount)}")
           break
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
    else:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))




