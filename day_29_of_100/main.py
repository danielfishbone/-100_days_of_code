from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def on_gen_button():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    data = f"{website_input.get()} | {username_input.get()} | {password_input.get()} \n"
    with open("day_29_of_100/data.txt", mode = "a") as file :
      file.writelines(data)
    website_input.delete(0,END) 
    password_input.delete(0,END) 
    

# ---------------------------- UI SETUP ------------------------------- #
 
window =  Tk()
window.config(
padx=50,pady=50)
window.title("Password Manager")
canvas = Canvas(width=200,height=200, highlightthickness=0)

image_path = "day_29_of_100/logo.png"
image = PhotoImage(file = image_path)
canvas.create_image(100,100,image = image)
canvas.grid(row=0,column=1)
website_label =Label(text="Website: ",font=("Arial",16,"normal"))
website_label.grid(row=1,column=0)
username_label =Label(text="Email/Username: ",font=("Arial",16,"normal"))
username_label.grid(row=2,column=0)
password_label =Label(text="password: ",font=("Arial",16,"normal"))
password_label.grid(row=3,column=0)

website_input = Entry()
website_input.config(width=38)
website_input.grid(row=1,column=1, columnspan=2)
website_input.focus()

username_input = Entry()
username_input.config(width=38)
username_input.grid(row=2,column=1, columnspan=2)
username_input.insert(0,"samuelscdaniel@gmail.com")
password_input =  Entry()
password_input.config(width=24)
password_input.grid(row=3,column=1)

generate_button = Button(text="Generate",command=on_gen_button, width=10)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",command=save_password, width=36)
add_button.grid(row=4,column=1, columnspan=2)


window.mainloop()
