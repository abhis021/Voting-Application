import tkinter as tk
from tkinter import simpledialog

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
    print("Name of candidate ", answer)
else:
    print("No Name available ?")

answer = simpledialog.askinteger("Candidate age", "What is the age of candidate ?",
                                 parent=application_window,
                                 minvalue=18, maxvalue=76)
if answer is not None:
    print("Age of candidate ", answer)
else:
    print("No age available ?")

answer = simpledialog.askinteger("Candidate Income", "What is candidate's Income?",
                               parent=application_window,
                               minvalue=0, maxvalue=100000)
if answer is not None:
    print("Your Income is ", answer)
elif answer == 0:
    print("You don't have an Income, how do you propose that you will fund yourself for election?")

else:
    print("nigga")
    
