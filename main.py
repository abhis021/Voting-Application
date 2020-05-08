import tkinter as tk
from tkinter import messagebox

def text_box():
    if tk.messagebox.askokcancel(title="Voting App", message="Enter no. of Candidates"):
        root.destroy()
root=tk.Tk()
button=tk.Button(root,text="Press the Button", command =text_box)
button.pack()
root.mainloop()