from tkinter import *



BACKGROUND_COLOR = "#B1DDC6"















#----------------------------UI-------------------------------------
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263 , image=front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
timer_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)


window.mainloop()







