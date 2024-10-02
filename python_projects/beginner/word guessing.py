import random

name = input("Enter your name: ")
print("All the best!!", name)


words = ['apple', 'bicycle', 'candle', 'dragon', 'elephant', 'forest', 'honey', 'guitar',
         'island', 'lemon', 'mountain', 'notebook', 'piano', 'sunflower', 'rose', 'lion']


word = random.choice(words)

print("Guess the characters.....")


guesses = ''
chances = 12


while chances > 0:
    wrong = 0

    # Print each character or a blank underscore
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            wrong += 1

    print()


    if wrong == 0:
        print("You win!")
        break


    guess = input("Guess a character: ")


    if guess not in guesses:
        guesses += guess


    if guess not in word:
        chances -= 1
        print("Wrong guess!")
        print("You have", chances, "more guesses.")


    if chances == 0:
        print("You lose!")


print("The word was:", word)
