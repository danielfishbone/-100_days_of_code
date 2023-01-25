import tkinter

window = tkinter.Tk()
window.title("Tkinter Tutlorial")
window.minsize(width=800,height=500)

#creating a label
my_label = tkinter.Label(text="Label",font=("Arial",30,"normal"))
my_label.pack(side="right")





window.mainloop()