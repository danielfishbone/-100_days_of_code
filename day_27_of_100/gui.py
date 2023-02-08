import tkinter

window = tkinter.Tk()
window.title("Tkinter Tutlorial")
window.minsize(width=800,height=500)

#creating a label
my_label = tkinter.Label(text="Label",font=("Arial",30,"normal"))
my_label.pack()

my_label["text"] = "this is a new label"
input = tkinter.Entry()
input.pack()



def on_button():
    print("button clicked")
    print(add(9,9,8,7,6,5,4,3,2,1))
    my_label["text"] = input.get()
button = tkinter.Button(text="add",command=on_button)
button.pack()


# *args 

# example function
# the * in the *args parameter tells python to accept unlimited arguments
def add(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add(9,9,8,7,6,5,4,3,2,1))

# *kwargs 

# example function
# the * in the *args parameter tells python to accept unlimited keyword arguments



window.mainloop() 