from textwrap import fill
from tkinter import *
from turtle import title
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window =  Tk()
window.config(
padx=100,pady=50,bg = PINK)
window.title("Pomodoro")
canvas = Canvas(width=200,height=224,bg = PINK,highlightthickness=0)

image_path = "day_28_of_100/tomato.png"
image = PhotoImage(file = image_path)
canvas.create_image(100,112,image = image)
canvas.create_text(100,137,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()





window.mainloop()