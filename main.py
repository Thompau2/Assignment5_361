import tkinter as tk
import login


base = tk.Tk()
base.title('SAGE: Stress, Anxiety, and Goal Emulator')
base.configure(bg='#333333')
base.geometry('1920x1080')
login.login_screen(base)


base.mainloop()
