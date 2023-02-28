from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def on_gen_button():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    data = f"{website} | {username} | {password} \n"

    is_ok = messagebox.askokcancel(title=website,message=f"website:{website}\npassword: {password} \nusername: {username}\nDo you wish to save? ")

    if is_ok: 
      if len(website) != 0 and  len(username) != 0 and len(password) != 0:
        with open("day_29_of_100/data.txt", mode = "a") as file :
          file.writelines(data)
        website_input.delete(0,END) 
        password_input.delete(0,END) 
      else:
        messagebox.showwarning(title="Error Saving",message="please ensure none of the fields are empty")  
    

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
