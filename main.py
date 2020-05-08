import tkinter as tk
#from tkinter import messagebox
from tkinter import simpledialog

#def text_box():
#    if tk.messagebox.askokcancel(title="Voting App", message="Enter no. of Candidates"):
#        root.destroy()
#root=tk.Tk()
#button=tk.Button(root,text="Press the Button", command =text_box)
#button.pack()
#root.mainloop()

application_window = tk.Tk()

answer = simpledialog.askinteger("Voting Application", "Enter the number of candidates: ",
                                parent=application_window,
                                minvalue=0, maxvalue=100)
if answer is not None:
    print("The number of Candidates: ", answer)
else:
    print("There are no candidates ?")

answer = simpledialog.askstring("Candidate names", "What is the name of candidate ?",
                                 parent=application_window)
if answer is not None:
    print("Age of candidate ", answer)
else:
    print("No age available ?")

answer = simpledialog.askinteger("Candidate Income", "What is candidate's Income?",
                               parent=application_window,
                               minvalue=0, maxvalue=100000)
if answer is not None:
    print("Your Income is ", answer)
else:
    print("You don't have an Income, how do you propose that you will fund yourself for election?")