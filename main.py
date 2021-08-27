from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("./data/french_words.csv")
data_dict = df.to_dict()
index = 0

#--------------------Pick a random word----------------------------
def pick_a_word():
    global index
    index = random.randint(0, 100)
    fr_word = data_dict.get('French').get(index)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    window.after(3000, card_flip)


#-------------------card flip mechanism---------------------------
def card_flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    en_word = data_dict.get('English').get(index)
    canvas.itemconfig(word_text, text=en_word, fill="white")











#----------------------------UI-------------------------------------
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)




canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,263 , image=front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=pick_a_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_a_word)
right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)


window.mainloop()







