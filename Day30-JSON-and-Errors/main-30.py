import tkinter
from tkinter import messagebox
import random
import json

# CONSTANTS
ENTRY_WIDTH = 45
LABEL_TEXTS = ["Website", "Email/Username", "Password"]
RANDOM_MIN = 2
RANDOM_MAX = 4


class PasswordApp:
    def __init__(self):
        self.window = tkinter.Tk()

        self.canvas = None
        self.site_input = None
        self.username_input = None
        self.password_input = None
        self.logo_img = None

        self.setup_ui()

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def password_gen(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
        self.password_input.delete(0, tkinter.END)
        self.password_input.insert(0, password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password(self):
        new_data = {self.site_input.get():
            {
                "email": self.username_input.get(),
                "password": self.password_input.get()
            }
        }

        try:
            with open("my-passwords.json", "r") as file:  # Create Data_dict from file
                data_dict = json.load(file)
        except FileNotFoundError:
            with open("my-passwords.json", "w") as file:  # Create Data_dict and file.
                data_dict = {}
                json.dump(data_dict, file)
        finally:
            data_dict.update(new_data)  # Update Data_dict with new pass.

        with open("my-passwords.json", "w") as file:
            json.dump(data_dict, file, indent=4)  # Update the file.

        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_input.get())
        messagebox.showinfo(title="Success", message="Password saved and copied to clipboard.")

    def search_password(self):
        with open("my-passwords.json", "r") as file:
            data_dict = json.load(file)

        site = self.site_input.get()
        user = self.username_input.get()
        try:
            site_info = data_dict[site]
            if not user == site_info["email"]:
                raise KeyError
        except KeyError:
            messagebox.showerror(title="Not Found", message=f"That site and user combination, {site} | {user}, is not "
                                                            f"found in the records.")
        else:
            self.password_input.delete(0, tkinter.END)
            self.password_input.insert(0, site_info["password"])

    # ---------------------------- UI SETUP ------------------------------- #
    def setup_ui(self):
        self.window.title("My Password Program")
        self.window.config(padx=20, pady=20)
        self.window.columnconfigure(0, uniform="a")
        self.window.columnconfigure(1, uniform="a")
        self.window.columnconfigure(2, uniform="a")

        self.canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
        self.logo_img = tkinter.PhotoImage(file="logo.png")
        self.canvas.grid(column=1, row=0)
        self.canvas.create_image(100, 100, image=self.logo_img)

        site_label = tkinter.Label()
        site_label.config(text="Website")
        site_label.grid(column=0, row=1)

        self.site_input = tkinter.Entry()
        self.site_input.config(width=27)
        self.site_input.grid(column=1, row=1, columnspan=2, sticky="w")
        self.site_input.focus()

        search_button = tkinter.Button()
        search_button.config(text="Search", height=1, font=("Arial", 8), command=self.search_password)
        search_button.grid(column=2, row=1, sticky="w", padx=20)

        username_label = tkinter.Label()
        username_label.config(text="Email/Username")
        username_label.grid(column=0, row=2)

        self.username_input = tkinter.Entry()
        self.username_input.config(width=45)
        self.username_input.grid(column=1, row=2, columnspan=2, sticky="w")
        self.username_input.insert(0, "robin.b.sizemore@outlook.com")

        password_label = tkinter.Label()
        password_label.config(text="Password")
        password_label.grid(column=0, row=3)

        self.password_input = tkinter.Entry()
        self.password_input.config(width=27)
        self.password_input.grid(column=1, row=3, sticky="w")

        generate_button = tkinter.Button()
        generate_button.config(text="Generate Password", height=1, font=("Arial", 8), command=self.password_gen)
        generate_button.grid(column=2, row=3, sticky="w", padx=20)

        add_button = tkinter.Button()
        add_button.config(text="Add", command=self.save_password)
        add_button.grid(column=1, row=4)


app = PasswordApp()
app.window.mainloop()
