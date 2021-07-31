from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# application_window = tk.Tk()

# answer= simpledialog.askinteger("Voting Application", "Enter the number of candidates:", minvalue=1, maxvalue=30)
# if answer is not None:
#     messagebox.askokcancel("Voting Application", "The number of candidates:", answer)
# else:
#     messagebox.askokcancel("Voting Application", "There are no candidates? ")

# answer=simpledialog.askstring("Voting Application", "What is the name of Candidate?")

# if answer is not None:
#     messagebox.askokcancel("Voting Application", "Candidate name is", answer)
# else:
#     messagebox.askokcancel("Voting Application", "Candidate has no name?")

# answer=simpledialog.askinteger("Voting Application", "What is the candidate's age?", minvalue=18, maxvalue=76)

# if answer is not None:
#     messagebox.askokcancel("Voting Application", "Candidate's age is" , answer)
# else:
#     messagebox.askokcancel("Voting Application", "No age available")

# answer=simpledialog.askstring("Voting Application", "Who do you want to vote for? Enter Name")

# messagebox.askokcancel("Voting Application", "And the Vote is casted for ", answer)


class VoteApplication:
    def __init__(self, root):
        self.root = root
        self.root.title = "Voting Application"

        self.root.geometry("1200x700+200+150")

        self.filename = None
        self.title = StringVar()
        self.status = StringVar()

        self.titlebar = Label(self.root, textvariable=self.title, font=(
            "times new roman", 15, "bold"), bd=2, relief=GROOVE)

        self.titlebar.pack(side=TOP, fill=BOTH)

        self.settitle()

        self.statusbar = Label(self.root, textvariable=self.status, font=(
            "times new roman", 15, "bold"), bd=2, relief=GROOVE)

        self.statusbar.pack(side=BOTTOM, fill=BOTH)
        self.status.set("Welcome to Voting Application")

        self.menubar = Menu(self.root, font=(
            "times new roman", 15, "bold"), activebackground="navyblue")
        self.root.config(menu=self.menubar)

        # Creating File Menu
        self.filemenu = Menu(self.menubar, font=(
            "times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding New file Command
        self.filemenu.add_command(
            label="New", accelerator="Ctrl+N", command=self.newfile)
        # Adding Open file Command
        self.filemenu.add_command(
            label="Open", accelerator="Ctrl+O", command=self.openfile)
        # Adding Save File Command
        self.filemenu.add_command(
            label="Save", accelerator="Ctrl+S", command=self.savefile)
        # Adding Save As file Command
        self.filemenu.add_command(
            label="Save As", accelerator="Ctrl+A", command=self.saveasfile)
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(
            label="Exit", accelerator="Ctrl+E", command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Creating Edit Menu
        self.editmenu = Menu(self.menubar, font=(
            "times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding Cut text Command
        self.editmenu.add_command(
            label="Cut", accelerator="Ctrl+X", command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(
            label="Copy", accelerator="Ctrl+C", command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(
            label="Paste", accelerator="Ctrl+V", command=self.paste)
        # Adding Seprator
        self.editmenu.add_separator()
        # Adding Undo text Command
        self.editmenu.add_command(
            label="Undo", accelerator="Ctrl+U", command=self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Creating Help Menu
        self.helpmenu = Menu(self.menubar, font=(
            "times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding About Command
        self.helpmenu.add_command(label="About", command=self.infoabout)
        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # Creating Scrollbar
        scrol_y = Scrollbar(self.root, orient=VERTICAL)
        # Creating Text Area
        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=(
            "times new roman", 15, "bold"), state="normal", relief=GROOVE)
        # Packing scrollbar to root window
        scrol_y.pack(side=RIGHT, fill=Y)
        # Adding Scrollbar to text area
        scrol_y.config(command=self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill=BOTH, expand=1)

        # Calling shortcuts funtion
        self.shortcuts()

    def settitle(self):
        # Checking if Filename is not None
        if self.filename:
        # Updating Title as filename
            self.title.set(self.filename)
        else:
        # Updating Title as Untitled
            self.title.set("Untitled")
    def newfile(self,*args):
        # Clearing the Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling settitle funtion
        self.settitle()
        # updating status
        self.status.set("New File Created")
    def openfile(self,*args):
        try:
            self.filename = filedialog.askopenfilename(title = "Select File", filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))

            if self.filename:
                infile = open(self.filename, "r")
                self.txtarea.delete("1.0", END)
                for line in infile:
                    self.txtarea.insert(END, line)
                infile.close()

                self.settitle()
                self.status.set("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    def savefile(self,*args):
        try:
            if self.filename:
                data = self.txtarea.get("1.0", END)

                outfile = open(self.filename, "w")

                outfile.write(data)

                outfile.close()

                self.settitle()

                self.status.set("Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception", e)
    def saveasfile(self, *args):
        try:
            untitledfile = filedialog.asksaveasfilename(title = "Save File As", defaultextension = "txt", initialfile = "Untitled.txt", filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            data = self.txtarea.get("1.0", END)

            outfile = open(untitledfile, "w")
            outfile.write(data)
            outfile.close()

            self.filename = untitledfile
            self.settitle()
            self.status.set("Saved Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)
    def exit(self, *args):
        op = messagebox.askyesno("Warning", "Your Unsaved Data May be Lost!")
        if op>0:
            self.root.destroy()
        else:
            return
    def cut(self, *args):
        self.txtarea.event_generate("<<Cut>>")
    def copy(self, *args):
        self.txtarea.event_generate("<<Copy>>")
    def paste(self, *args):
        self.txtarea.event_generate("<<Paste>>")
    def undo(self, *args):
        try:
            if self.filename:
                self.txtarea.event_generate("1.0", END=True)
                infile = open(self.filename,"r")
                for line in infile:
                    self.txtarea.insert(END, line)
                infile.close()

                self.settitle()

                self.status.set("Undone Successfully")
            else:
                self.txtarea.delete("1.0", END)
                self.filename = None
                self.settitle()
                self.status.set("Undone Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)
    def infoabout(self):
        messagebox.showinfo("About Voting Application", "A simple vote processing application that stores votes.")
            


    def shortcuts(self):
        # Binding Ctrl+n to newfile funtion
        self.txtarea.bind("<Control-n>",self.newfile)
        # Binding Ctrl+o to openfile funtion
        self.txtarea.bind("<Control-o>",self.openfile)
        # Binding Ctrl+s to savefile funtion
        self.txtarea.bind("<Control-s>",self.savefile)
        # Binding Ctrl+a to saveasfile funtion
        self.txtarea.bind("<Control-a>",self.saveasfile)
        # Binding Ctrl+e to exit funtion
        self.txtarea.bind("<Control-e>",self.exit)
        # Binding Ctrl+x to cut funtion
        self.txtarea.bind("<Control-x>",self.cut)
        # Binding Ctrl+c to copy funtion
        self.txtarea.bind("<Control-c>",self.copy)
        # Binding Ctrl+v to paste funtion
        self.txtarea.bind("<Control-v>",self.paste)
        # Binding Ctrl+u to undo funtion
        self.txtarea.bind("<Control-u>",self.undo)


root = Tk()
VoteApplication(root)

root.mainloop()
