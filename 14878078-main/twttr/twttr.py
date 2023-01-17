tweet = input("Enter your tweet: ")

tweet_lst = tweet.split(" ")
vowels = ['a', 'e', 'i', 'o', 'u']
new_lst = []

for word in tweet_lst:
    new_word = ""
    for i in range(0, len(word)):
        if word[i].lower() in vowels:
            pass
        else:
            new_word += word[i]
    new_lst.append(new_word)

print(" ".join(new_lst))


