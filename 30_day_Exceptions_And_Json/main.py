from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #stuff that will be dumped to json file
    #json is pretty much storing stuff in a dictionary
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #using json to store stuff instead
        #change to "r" read mode for json.load
        try:
            with open("30_day_Exceptions_And_Json/data.json", "r") as data_file:
        #indent = 4 makes json file easier to read
            #json.dump(new_data, data_file, indent=4)
        #now that there is data in json file, try to read from json file
            #data = json.load(data_file)
            #print(data)#data is stored as a python dictionary
        #at this point, learned json dump,load, and now update so we can add to a json file
        #need to load up the existing data
                data = json.load(data_file)#reading old data
        except FileNotFoundError:
            with open("30_day_Exceptions_And_Json/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:  
            data.update(new_data)#updating old data

            with open("30_day_Exceptions_And_Json/data.json", "w") as data_file:    
            #now that data is added to data_file, need to actually write the data back to file using dump
                json.dump(data,data_file, indent=4)#saving updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
        #                                               f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        #     with open("30_day_Exceptions_And_Json/data.txt", "a") as data_file:
        #         data_file.write(f"{website} | {email} | {password}\n")
        #         website_entry.delete(0, END)
        #         password_entry.delete(0, END)

#open json, search using input from website input, make pop up for password and stuff,
def search_website_list():
    website = website_entry.get()
    with open("30_day_Exceptions_And_Json/data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="30_day_Exceptions_And_Json/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=17)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_websites_button = Button(text="Search", command=search_website_list)
search_websites_button.grid(row=1, column = 2, columnspan=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()