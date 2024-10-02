import random

def number_guess_game():
    guessing_number = random.randint(1,100)
    chances = 7

    print("Welcome to the number guessing game!")
    print("Note: You only have 7 chances to guess the number......")
    print("Guess a number from 1 to 100")

    for chance in range(1,chances+1):
        try:
            guess = int(input(f"Attempt {chance}/{chances}: Enter your guess: "))

            if guess< guessing_number:
                print("Too low!! try again")
            elif guess>guessing_number:
                print("Too high!! try again")
            else:
                print(f"Congratulations! You have guessed the number in {chance} attempts")
                break
        except ValueError:
            print("Please enter a valid number")

        if chance == chances:
            print(f"Sorry, your chances are finished. The number was {guessing_number}")

number_guess_game()
