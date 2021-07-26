import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}")  # if user_name.get() returns None prints World instead of it


root = tk.Tk()
root.title('Hello')

user_name = tk.StringVar()

greet_label = ttk.Label(root, text='Name: ')
greet_label.pack(side='left', padx=(0, 10))  # padx=(0, 10) adds 10px to the right of the label

name_entry = ttk.Entry(root, width=15, textvariable=user_name)  # saves entered value to user_name variable
name_entry.pack(side='left')

greet_button = ttk.Button(root, text='Greet', command=greet)
greet_button.pack(side='left', fill='x', expand=True)

exit_button = ttk.Button(root, text='Exit', command=root.destroy)
exit_button.pack(side='left', fill='x', expand=True)

root.mainloop()