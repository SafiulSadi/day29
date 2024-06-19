# import pandas
#
# data = pandas.read_csv("book1.csv")
# x = data["tee_cost"].to_list()
# av =[]
# for i in x:
#     av.append(i+10)
#
# print(av)
# df = pandas.DataFrame(av)
# df.to_csv("rusho.csv")
# print(df)

from tkinter import *
import random
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    letter_list = [random.choice(letters) for letter in range(nr_letters)]
    symbols_list = [random.choice(symbols) for symbol in range(nr_symbols)]
    number_list = [random.choice(numbers) for number in range(nr_numbers)]
    password_list = letter_list + symbols_list + number_list
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def open_and_save_to_file(line):
    with open("passwords.txt", "a") as file:
        file.write(line)



def save_password():
    website_entry_text = website_entry.get()
    username_entry_text = username_entry.get()
    password_entry_text = password_entry.get()
    answer = False
    if website_entry_text == "" or username_entry_text == "" or password_entry_text == "":
        messagebox.showinfo(title="Oops", message="Do not leave any of the fields empty")
    else:
        text_str = website_entry_text + " | " + username_entry_text + " | " + password_entry_text + "\n"
        print(text_str)
        answer = messagebox.askyesno(title=website_entry_text,
                                     message=f"These are the details entered:\nEmail: {username_entry_text}\nPassword: {password_entry_text} \nIs it okay to save?")
        print(answer)
        if answer:
            open_and_save_to_file(text_str)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# label = Label(text="Password Manager", font=("Arial", 50, "bold"))
# label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.delete(0, END)
username_entry.insert(0, "safiul.sadi@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# Buttons
generate_btn = Button(text="Generate", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add",width=36, command=save_password)
add_btn.grid(column=0, row=4, columnspan=2)




window.mainloop()
