from random import choice

word = choice(["code", "club", "robot", "party"])

guessed = []
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + " _ "

    if out == word:
        break

    print("Guess the word:", out)
    print(tries, "chances left")

    guess = input()
    if guess == word:
        print ("Welldone")
        break

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("You guessed", word)
else:
    print("You didn't get", word)