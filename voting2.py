import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

application_window=tk.Tk()

answer= simpledialog.askinteger("Voting Application", "Enter the number of candidates:", minvalue=1, maxvalue=30)

if answer is not None:
    messagebox.askokcancel("Voting Application", "The number of candidates:"+answer)
else:
    messagebox.askokcancel("Voting Application", "There are no candidates? ")

answer=simpledialog.askstring("Voting Application", "What is the name of Candidate?")

if answer is not None:
    messagebox.askokcancel("Voting Application", "Candidate name is"+answer)
else:
    messagebox.askokcancel("Voting Application", "Candidate has no name?")

answer=simpledialog.askinteger("Voting Application", "What is the candidate's age?", minvalue=18, maxvalue=76)

if answer is not None:
    messagebox.askokcancel("Voting Application", "Candidate's age is" , answer)
else:
    messagebox.askokcancel("Voting Application", "No age available")

answer=simpledialog.askokcancel("Voting Application", "Who do you want to vote for? Enter Name")

messagebox.askokcancel("Voting Application", "And the Vote is casted for ", answer)
