from audioop import cross
from tkinter import *
import random
import pandas as pd
import json
import time

BACKGROUND_COLOR = "#B1DDC6"

words_to_learn = pd.DataFrame()

#read in csv with pandas
try:
    flashcard_word_data = pd.read_csv("31_day_capstone_flashcards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("31_day_capstone_flashcards/data/french_words.csv")
    flashcard_word_data = original_data.copy()
    words_to_learn = original_data.copy()
else:
    words_to_learn = flashcard_word_data.copy()

#global
current_card = pd.DataFrame()


##functions

#get random index in list of words
def random_word_pair_index():
    global words_to_learn
    return random.randint(0,100)

#generate a new flashcard and display new data
def new_flashcard():
    #word_pair = flashcard_word_data[flashcard_word_data.index == random_word_pair_index()]
    rand_index = int(random.choice(words_to_learn.index))
    word_pair = flashcard_word_data.loc[[rand_index]]
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = word_pair
    french_word = word_pair["French"].values[0]
    #swap the card and corresponding text
    canvas.itemconfig(canvas_language_text, text="French", fill="black")
    canvas.itemconfig(canvas_word_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_card_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_flashcard)
    

def flip_flashcard():
    global current_card 
    word_pair = current_card
    english_word = word_pair["English"].values[0]
    #swap the card and corresponding text
    canvas.itemconfig(canvas_language_text, text="English", fill="white")
    canvas.itemconfig(canvas_word_text, text=english_word, fill="white")
    canvas.itemconfig(canvas_card_img, image=card_back_img)
    return

def word_is_known():
    global words_to_learn
    print(current_card)
    words_to_learn = words_to_learn.drop(index=int(current_card.index.values))
    #drop=True prevents adding another index column which would cause an error if one already exists
    words_to_learn = words_to_learn.reset_index(drop=True)
    words_to_learn.to_csv("31_day_capstone_flashcards/data/words_to_learn.csv", index=False)
    print(words_to_learn)
    new_flashcard()

#interface setup
window = Tk()
window.title("English->French Flashcards")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="31_day_capstone_flashcards/images/card_front.png")
card_back_img = PhotoImage(file="31_day_capstone_flashcards/images/card_back.png")
canvas_card_img = canvas.create_image(400, 263, image= card_front_img)


#text in card
canvas_language_text = canvas.create_text(400,150,text="title", font=("Ariel", 40, "italic"))
canvas_word_text = canvas.create_text(400,300,text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#check and cross buttons
cross_image = PhotoImage(file="31_day_capstone_flashcards/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_flashcard)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="31_day_capstone_flashcards/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=word_is_known)
known_button.grid(row=1, column=1)


##labels
#stuff for later
language_label = Label(text="language of word")
english_word_label = Label(text="english word")
french_word_label = Label(text="french word")

flip_timer = window.after(3000, func=flip_flashcard)

##program start
new_flashcard()

window.mainloop()
