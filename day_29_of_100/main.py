from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice
from random import randint
from password import letters, numbers, symbols
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def on_gen_button():
    nr_letters = 3
    nr_symbols = 2
    nr_numbers = 3

    list_of_char = []
    for sample in range(nr_letters):
        list_of_char.append("L")
    for sample in range(nr_symbols):
        list_of_char.append("S")
    for sample in range(nr_numbers):
        list_of_char.append("N")
    password = ""

    for i in range(len(list_of_char)):
        selected = randint(0, len(list_of_char) - 1)
        val = list_of_char.pop(selected)
        if val == "L":
            password += str(choice(letters))
        elif val == "S":
            password += str(choice(symbols))
        elif val == "N":
            password += str(choice(numbers))
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    website = website_input.get().capitalize()
    if len(website) > 0:
      try:
          with open("day_29_of_100/data.json", mode="r") as file:
              data = json.load(file)
      except FileNotFoundError:
          messagebox.showinfo(title="Error", message="No Database file found")

      except json.decoder.JSONDecodeError:
          messagebox.showinfo(title="Error", message="Database corrupt")
      else:
          try:
              username = data[website]["username"]
              password = data[website]["password"]
          except KeyError:
              messagebox.showerror(
                  title="Oops!", message=f"details for {website} was not found")

          else:
              messagebox.showinfo(
                  title=website, message=f"Username:{username}\nPassword: {password}")
    else:
        messagebox.showerror(
                  title="Oops!", message=f"Type in a keyword to search for in the website field")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get().capitalize()
    username = username_input.get()
    password = password_input.get()
    data_dict = {
        website: {
            "username": username,
            "password": password,
        }
    }

    is_ok = messagebox.askokcancel(
        title=website, message=f"website:{website}\npassword: {password} \nusername: {username}\nDo you wish to save? ")

    if is_ok:
        if len(website) != 0 and len(username) != 0 and len(password) != 0:
            try:
                with open("day_29_of_100/data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(data_dict)
            except FileNotFoundError:
                with open("day_29_of_100/data.json", mode="w") as file:
                    json.dump(data_dict, file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("day_29_of_100/data.json", mode="w") as file:
                    json.dump(data_dict, file, indent=4)
            else:
                with open("day_29_of_100/data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
        else:
            messagebox.showwarning(
                title="Error Saving", message="please ensure none of the fields are empty")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(
    padx=50, pady=50)
window.title("Password Manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)

image_path = "day_29_of_100/logo.png"
image = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
website_label = Label(text="Website: ", font=("Arial", 16, "normal"))
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username: ", font=("Arial", 16, "normal"))
username_label.grid(row=2, column=0)
password_label = Label(text="password: ", font=("Arial", 16, "normal"))
password_label.grid(row=3, column=0)

website_input = Entry()
website_input.config(width=24)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()

username_input = Entry()
username_input.config(width=38)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "samuelscdaniel@gmail.com")
password_input = Entry()
password_input.config(width=24)
password_input.grid(row=3, column=1)

search_button = Button(text="Search", command=search_password, width=10)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate", command=on_gen_button, width=10)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
