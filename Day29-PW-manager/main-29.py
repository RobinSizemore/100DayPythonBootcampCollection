import tkinter
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, tkinter.END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if site_input.get() == "" or username_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="ERROR!", message="Please input all fields.")
        return
    else:
        confirm = messagebox.askokcancel(title="All good?", message="Are you sure you want to save these details?")
        if not confirm:
            messagebox.showinfo(title="Canceled", message="Save has been canceled.")
            return

    with open("my-passwords.txt", "a") as file:
        file.writelines(f"{site_input.get()} | {username_input.get()} | {password_input.get()}\n")
    window.clipboard_clear()
    window.clipboard_append(password_input.get())
    messagebox.showinfo(title="Success", message="Password saved and copied to clipboard.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Password Program")
window.config(padx=20, pady=20)
window.columnconfigure(0, uniform="a")
window.columnconfigure(1, uniform="a")
window.columnconfigure(2, uniform="a")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="./logo.png")
canvas.grid(column=1, row=0)
canvas.create_image(100, 100, image=logo_img)

site_label = tkinter.Label()
site_label.config(text="Website")
site_label.grid(column=0, row=1)

site_input = tkinter.Entry()
site_input.config(width=45)
site_input.grid(column=1, row=1, columnspan=2, sticky="w")
site_input.focus()

username_label = tkinter.Label()
username_label.config(text="Email/Username")
username_label.grid(column=0, row=2)

username_input = tkinter.Entry()
username_input.config(width=45)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(0, "robin.b.sizemore@outlook.com")


password_label = tkinter.Label()
password_label.config(text="Password")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry()
password_input.config(width=27)
password_input.grid(column=1, row=3, sticky="w")

generate_button = tkinter.Button()
generate_button.config(text="Generate Password", height=1, font=("Arial", 8), command=password_gen)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button()
add_button.config(text="Add", command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()
