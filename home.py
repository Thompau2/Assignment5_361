import tkinter as tk
from PIL import Image, ImageTk


def home_screen(parent):

    def notes_pressed():
        print('notes')

    def goals_pressed():
        print('goals')

    def plans_pressed():
        print('plans')

    frame = tk.Frame(parent, bg='#333333')

    log_out_button = tk.Button(parent,text='LOG-OUT', bg='#333333',fg='#ffffff', borderwidth=0)
    logo_import = ImageTk.PhotoImage(Image.open('export-0001.png'))
    logo = tk.Label(frame, image=logo_import, borderwidth=0)

    page_title = tk.Label(frame, text='SAGE', bg='#333333', fg='#7383B2', font=('Arial', 32))

    # pull quotes from random quotes and put into row=1 column = 0
    quote = tk.Label(frame, text='This is to fill in the text space for a quote database to be inserted later',
                     bg='#333333', fg='#ffffff', wraplength=150)

    # put 3 main function buttons into next section row=2 column = 0,1,2
    notes_button = tk.Button(frame, text='notes', fg='#ffffff', bg='#7383B2', command=notes_pressed)
    goals_button = tk.Button(frame, text='goals', fg='#ffffff', bg='#7383B2', command=goals_pressed)
    plans_button = tk.Button(frame, text='plans', fg='#ffffff', bg='#7383B2', command=plans_pressed)

    log_out_button.pack()
    logo.grid(row=1, column=1, pady=10)
    page_title.grid(row=2, column=1, pady=20)
    quote.grid(row=3, column=1, pady=30)
    notes_button.grid(row=4, column=0, pady=40)
    goals_button.grid(row=4, column=1)
    plans_button.grid(row=4, column=2)
    frame.pack()


