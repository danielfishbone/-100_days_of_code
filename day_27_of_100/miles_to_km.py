import tkinter 
def on_button():
    pass
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=350,height=100)

mile_label = tkinter.Label(text="Miles",font=("Arial",16,"normal"))
mile_label.grid(row=2,column=3)

km_label = tkinter.Label(text="Km",font=("Arial",16,"normal"))
km_label.grid(row=1,column=3)

is_equal_label = tkinter.Label(text="is equal to",font=("Arial",16,"normal"))
is_equal_label.grid(row=2,column=1)

input = tkinter.Entry()
input.grid(row=1,column=2)

button = tkinter.Button(text="Calculate",command=on_button)
button.grid(row=3,column=2)

window.mainloop() 