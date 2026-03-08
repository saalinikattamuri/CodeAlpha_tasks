import random
import tkinter as tk
from words import word_list

# Select random word
word = random.choice(word_list)
display = ["_"] * len(word)
lives = 6

# Function to process guess
def guess_letter():
    global lives

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
    else:
        lives -= 1

    word_label.config(text=" ".join(display))
    lives_label.config(text=f"Lives left: {lives}")

    if "_" not in display:
        result_label.config(text="🎉 You Win!")
    elif lives == 0:
        result_label.config(text=f"💀 Game Over! Word was {word}")

# Create window
window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x300")

title = tk.Label(window, text="Hangman Game", font=("Arial", 20))
title.pack(pady=10)

word_label = tk.Label(window, text=" ".join(display), font=("Arial", 18))
word_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack(pady=5)

lives_label = tk.Label(window, text=f"Lives left: {lives}")
lives_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()