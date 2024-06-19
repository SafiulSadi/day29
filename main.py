# from tkinter import *
#
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
#
#
# def open_and_save_to_file(line):
#     with open("passwords.txt", "a") as file:
#         file.write(line)
#
#
#
# def save_password():
#     website_entry_text = website_entry.get()
#     username_entry_text = username_entry.get()
#     password_entry_text = password_entry.get()
#     text_str = website_entry_text + " | " +username_entry_text + " | " + password_entry_text + "\n"
#     print(text_str)
#     open_and_save_to_file(text_str)
#     website_entry.delete(0, END)
#     password_entry.delete(0, END)
#
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Password Manager")
# window.config(pady=50, padx=50)
#
# # label = Label(text="Password Manager", font=("Arial", 50, "bold"))
# # label.grid(column=1, row=0)
#
# canvas = Canvas(width=200, height=200)
# logo_image = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_image)
# canvas.grid(column=1, row=0)
#
# # Labels
# website_label = Label(text="Website: ")
# website_label.grid(column=0, row=1)
#
# username_label = Label(text="Email/Username: ")
# username_label.grid(column=0, row=2)
#
# Password_label = Label(text="Password: ")
# Password_label.grid(column=0, row=3)
#
#
# # Entries
# website_entry = Entry(width=35)
# website_entry.grid(column=1, row=1, columnspan=2)
# website_entry.focus()
#
#
# username_entry = Entry(width=35)
# username_entry.grid(column=1, row=2, columnspan=2)
# username_entry.delete(0, END)
# username_entry.insert(0, "safiul.sadi@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(column=1, row=3)
#
#
# # Buttons
# generate_btn = Button(text="Generate")
# generate_btn.grid(column=2, row=3)
#
# add_btn = Button(text="Add",width=36, command=save_password)
# add_btn.grid(column=0, row=4, columnspan=2)
#
#
#
#
# window.mainloop()
import pandas

data = pandas.read_csv("book1.csv")
x = data["tee_cost"].to_list()
av =[]
for i in x:
    av.append(i+10)

print(av)
df = pandas.DataFrame(av)
df.to_csv("rusho.csv")
print(df)