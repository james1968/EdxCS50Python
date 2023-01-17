def main():
    tweet = input("Enter your tweet: ")
    print(shorten(tweet))


def shorten(tweet):
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

    return(" ".join(new_lst))


if __name__ == "__main__":
    main()