from random import randrange

# Intro
print("Welcome to the Number Guessing Game!")
print("You must guess the correct number between 0 and 100.")
print("You have 10 tries per game to guess the number correctly.")

# main game loop
play_again = "Y"
while play_again == "Y" or play_again == "y":
    # Generate a random number from 0 to 100
    random_number = randrange(0, 101)
    guess_count = 0
    max_guesses = 10
    success = False

    # User guess loop (10 tries)
    while guess_count < max_guesses:
        guess_number = guess_count + 1
        print("Guess #" + str(guess_number) + ":")
        guess = int(input("Enter a number between 0 and 100: "))

        guess_count += 1

        if guess == random_number:
            print("Congratulations! You guessed the correct number in", guess_count, "tries!")
            success = True
            break
        elif guess < random_number:
            print("Incorrect. Try again! Hint: Your guess is too low.")
        else:
            print("Incorrect. Try again! Hint: Your guess is too high.")

    # If the user didn't guess it right in 10 tries
    if not success:
        print("You ran out of guesses. The correct number was", random_number)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Y/N): ")
    while play_again != "Y" and play_again != "y" and play_again != "N" and play_again != "n":
        play_again = input("Invalid input. Please enter 'Y' or 'N': ")

print("Completed by, Jennifer Mendoza Trejo")
