import tkinter

window = tkinter.Tk()
window.title("Tkinter Tutlorial")
window.minsize(width=800,height=500)

#creating a label
my_label = tkinter.Label(text="Label",font=("Arial",30,"normal"))
my_label.pack(side="right")


# *args 

# example function
def add(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add(9,9,8,7,6,5,4,3,2,1))
# window.mainloop()