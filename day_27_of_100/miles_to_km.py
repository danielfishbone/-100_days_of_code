import tkinter 
def on_button():
    global answer
    try:
        km =int(input.get())
        answer =km*0.621371
        answer_label.config(text=answer)
    except:    
        pass
window = tkinter.Tk()
window.title("Km to Mile Converter")
window.minsize(width=350,height=100)
answer = 0

mile_label = tkinter.Label(text="Miles",font=("Arial",16,"normal"))
mile_label.grid(row=1,column=5)

km_label = tkinter.Label(text="Km",font=("Arial",16,"normal"))
km_label.grid(row=1,column=2)

is_equal_label = tkinter.Label(text=" = ",font=("Arial",16,"normal"))
is_equal_label.grid(row=1,column=3)

answer_label = tkinter.Label(text=str(answer),font=("Arial",16,"normal"))
answer_label.grid(row=1,column=4)

input = tkinter.Entry()
input.config(width=6)
input.grid(row=1,column=1)

button = tkinter.Button(text="Calculate",command=on_button)
button.grid(row=3,column=3)

window.mainloop() 