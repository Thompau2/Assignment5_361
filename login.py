import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import home


def login_screen(parent):

    def login_attempt():
        if username_entry.get() != '' and password_entry != '':
            messagebox.showinfo(title='Success', message='You have logged in')
            frame.forget()
            home.home_screen(parent)
        else:
            messagebox.showerror(title='Error', message='Invalid Login')

    frame = tk.Frame(parent, bg='#333333')

    logo_import = ImageTk.PhotoImage(Image.open('export-0001.png'))
    logo = tk.Label(frame, image=logo_import, borderwidth=0)

    page_title = tk.Label(frame, text='Login', bg='#333333', fg='#7383B2', font=('Arial', 32))
    username_text = tk.Label(frame, text='Username', bg='#333333', fg='#ffffff')
    username_entry = tk.Entry(frame)
    password_text = tk.Label(frame,text='Password', bg='#333333', fg='#ffffff')
    password_entry = tk.Entry(frame, show='*')
    login_button = tk.Button(frame, text='Login', bg='#7383B2', fg='#ffffff', command=login_attempt)
    create_label = tk.Label(frame, text="Don't have an account for this device?", bg='#333333', fg='#ffffff')
    create_button = tk.Button(frame, text='Create one here!', bg='#333333', fg='#1589FF', borderwidth=0)

    logo.grid(row=0, column=0, pady=10)
    page_title.grid(row=1, column=0, pady=20)
    username_text.grid(row=2, column=0)
    username_entry.grid(row=3, column=0)
    password_text.grid(row=4, column=0)
    password_entry.grid(row=5, column=0)
    login_button.grid(row=6, column=0, pady=30)
    create_label.grid(row=7, column=0)
    create_button.grid(row=8, column=0)

    frame.pack()
