def main():
    word = input("Word to shorten: ")
    print(shorten(word))


def shorten(word):
    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(i, "")
    return word
    
if __name__ == "__main__":
    main()