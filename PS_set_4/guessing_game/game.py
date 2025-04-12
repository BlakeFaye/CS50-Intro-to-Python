from random import randint

while True:
    try:
        level = int(input("Level: "))
        break

    except ValueError:
        continue

myst_num = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > myst_num:
            print("Too large!")
            continue

        elif guess < myst_num:
            print("Too small!")
            continue

        else:
            print("Just right!")
            break

    except ValueError:
        continue


