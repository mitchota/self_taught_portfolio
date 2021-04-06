# Self-Taught Programmer Assignment 2 - Guess a Number

answers = [1, 2, 3, 5, 7, 11, 13, 17, 19]



while True:

    guess = input("Give me a number (q to quit): ")

    if guess == "q":

        break

    guess = int(guess)

    if guess not in answers:

        print("I can't seem to find it. Try again.")

    else:

        print("Good job. You found it!")

        break