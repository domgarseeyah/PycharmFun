from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#qweqwe

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_char = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]
    # password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_num + password_char + password_letters
    random.shuffle(password_list)

    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password_entry.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data_dic = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oopsies", message="Please don't leave inputs blank")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n "
        #                                               f"Password: {password}\n Is it okay to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data_dic, data_file, indent=4)
        else:
            data.update(new_data_dic)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # json.load(data_file)
            # data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#making a change hahahah
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        website = website_entry.get()
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}, \n password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no detail for {website}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
canvas = Canvas(width=200, height=200)
window.config(padx=50, pady=30)

logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
site_label = Label(text="Website: ")
site_label.grid(column=0, row=1)
email_label = Label(text="Email Address/User Name: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# EntryBoxes
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dgarcia")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons
search_json = Button(text="Website Lookup", width=16, command=find_password)
search_json.grid(column=2, row=1)
generating_password = Button(text="Generate Password", width=16, command=generate_password)
generating_password.grid(column=2, row=3)
add_new_record = Button(text="Add", width=35, command=save)
add_new_record.grid(column=1, row=4, columnspan=2)


window.mainloop()
