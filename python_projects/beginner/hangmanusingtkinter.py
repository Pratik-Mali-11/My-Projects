import tkinter as tk
import random

words = ['apple', 'bicycle', 'candle', 'dragon', 'elephant', 'forest', 'honey', 'guitar',
         'island', 'lemon', 'mountain', 'notebook', 'piano', 'sunflower', 'rose', 'lion']

def start_game():
    global word,guesses,chances
    word = random.choice(words)
    guesses = ''
    chances = 7

    word_Label.config(text="_"*len(word))
    chances_Label.config(text=f"chances left:{chances}")
    message_Label.config(text="")
    entry.config(state="normal")
    play_again_button.pack_forget()
    exit_button.pack_forget()


def update_display():
    display_word = ''
    for char in word:
        if char in guesses:
            display_word+=char+' '
        else:
            display_word +="_"
    word_Label.config(text=display_word)

    chances_Label.config(text=f"chances left:{chances}")

    if '_' not in display_word:
        message_Label.config(text="You winn!")
        entry.config(state='disabled')
        show_end_buttons()

def check_guess():
    global chances, guesses
    guess = entry.get().lower()

    if guess.isalpha() and len(guess)==1 and guess not in guesses:
        guesses+=guess
        if guess not in word:
            chances-=1

        update_display()
        entry.delete(0,tk.END)

        if chances == 0:
            message_Label.config(text="You lose....")
            word_Label.config(text = f"the word was:{word}")
            entry.config(state='disabled')
            show_end_buttons()

def show_end_buttons():
    play_again_button.pack(pady=10)
    exit_button.pack(pady=10)

def exit_game():
    window.destroy()

window = tk.Tk()
window.title('hangman')

word_Label = tk.Label(window,text="_"*len(words[0]),font=("Arail",24))
word_Label.pack(pady=20)

chances_Label = tk.Label(window,text=f"Chances left: 7",font=("Arial",16))
chances_Label.pack(pady=10)

entry_Label = tk.Label(window,text ="Enter a letter: ",font=("Arial",14))
entry_Label.pack()

entry = tk.Entry(window,font=("Arial",14))
entry.pack()

submit_button=tk.Button(window,text="Guess",command = check_guess,font=("Arial",14))
submit_button.pack(pady=10)

message_Label = tk.Label(window,text = "",font=("Arial",16))
message_Label.pack(pady=20)

play_again_button = tk.Button(window,text="Play again..",command=start_game,font=("Arial",14))
exit_button = tk.Button(window,text="Exit",command = exit_game,font=("Arial",14))

start_game()
window.mainloop()