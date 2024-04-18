from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_list = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    word_list = original_df.to_dict(orient="records")
else:
    word_list = df.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    current_card = random.choice(word_list)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_picture)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_picture)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text =current_card["English"], fill="white")


def is_known():
    word_list.remove(current_card)
    data = pd.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)


card_front_picture = PhotoImage(file="images/card_front.png")
card_back_picture = PhotoImage(file="images/card_back.png")
right_button_picture = PhotoImage(file="images/right.png")
wrong_button_picture = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 262, image=card_front_picture)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_button_picture, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_button_picture, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


next_card()

window.mainloop()


