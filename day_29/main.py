from tkinter import *
import json
from tkinter import messagebox, simpledialog
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_array = [choice(letters) for _ in range(randint(8, 10))]
    symbols_array = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_array = [choice(numbers) for _ in range(randint(2, 4))]

    new_password = letters_array + symbols_array + numbers_array
    shuffle(new_password)

    password = "".join(new_password)
    if len(password_input.get()) == 0:
        password_input.insert(0, password)
        password_input.clipboard_append(password)
    else:
        password_input.delete(0, END)
        password_input.insert(0, password)
        password_input.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_get = website_input.get()
    username_get = email_input.get()
    password_get = password_input.get()
    new_data = {
        website_get: {
            "email": username_get,
            "password": password_get
        }
    }

    if (len(website_get) > 0 and len(password_get) > 0):
        try:
            with open("passwords.json", 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open("passwords.json", 'w') as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", 'w') as json_file:
                json.dump(data, json_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(
            title="Warning", message="Please populate all of these fields.")


# ---------------------------- SEARCH ------------------------------- #

def search_websites():
    searched_phrase = website_input.get().capitalize()
    if len(searched_phrase) > 0:
        try:
            with open("passwords.json", 'r') as json_file:
                data_to_search = json.load(json_file)
        except FileNotFoundError:
            messagebox.showinfo(title=":(", message=f"Not found password DB")
        else:
            if searched_phrase in data_to_search:
                email = data_to_search[searched_phrase]["email"]
                password = data_to_search[searched_phrase]["password"]
                messagebox.showinfo(title=f"{searched_phrase}",
                                message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=80)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=3)


website_label = Label(text="Webiste:")
website_label.grid(row=3, column=2)
website_input = Entry(width=35)
website_input.grid(row=3, column=3, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=4, column=2)
email_input = Entry(width=35)
email_input.insert(0, "ervin@ervin.com")
email_input.grid(row=4, column=3, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=5, column=2)
password_input = Entry(width=21)
password_input.grid(row=5, column=3)

generate_button = Button(text="Search",
                         width=10, command=search_websites)
generate_button.grid(row=3, column=4)

generate_button = Button(text="Generate Password",
                         width=10, command=generate_password)
generate_button.grid(row=5, column=4)

save_button = Button(text="Save", width=33, command=save_password)
save_button.grid(row=6, column=3, columnspan=2)


window.mainloop()
