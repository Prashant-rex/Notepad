from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
	global file
	root.title("Untitled")
	file = None
	TextArea.delete(1.0,END)
	# 1.0,END Delete all from 1st line 0th character to END


def openfile():
	global file
	file = askopenfilename(defaultextension = ".txt",filetypes = [("All Files", "*.*"),("Text Documents","*.txt")])
	if (file == ""):
		file = None
	else:
		root.title(os.path.basename(file)+" - Notepad")
		TextArea.delete(1.0,END)
		f = open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()

def savefile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt",filetypes = [("All Files", "*.*"),("Text Documents","*.txt")])
		if file == "":
			file = None
		else:
			# Save as a new file
			f = open(file,"w")
			f.write(TextArea.get(1.0,END))
			f.close()
			root.title(os.path.basename(file)+" - Notepad")
	else:
		# Save the file
		f = open(file,"w")
		f.write(TextArea.get(1.0,END))
		f.close()
def quitApp():
	root.destroy()


def cut():
	TextArea.event_generate(("<<Cut>>"))


def copy():
	TextArea.event_generate(("<<Copy>>"))



def paste():
	TextArea.event_generate(("<<Paste>>"))



def about():
	showinfo("Notepad","Created By Prashant-rex")
	# showinfo first argument is titleName

def rightClickFun(event):
	rightclick.tk_popup(event.x_root,event.y_root)
	rightclick.grab_release()



if __name__== '__main__':
	root = Tk()
	root.title("Untitled - Notepad")
	root.geometry("720x720")



	# Text Area
	TextArea = Text(root,font = "lucida 13")
	file = None
	TextArea.pack(expand = True,fill = BOTH)

	# Menu bar
	MenuBar = Menu(root)
	FileMenu = Menu(MenuBar,tearoff = 0)
	# tearoff remove undock command

	# Open New File
	FileMenu.add_command(label = "New",command = newFile)

	# Open already existing file
	FileMenu.add_command(label = "Open",command = openfile)

	# Save current file
	FileMenu.add_command(label = "Save",command = savefile)
	
	FileMenu.add_separator()
	
	FileMenu.add_command(label = "Exit",command = quitApp)
	
	# Add cascade stick all the menu to label File here
	MenuBar.add_cascade(label = "File",menu = FileMenu)

	#File Menu ends

	#Edit Menu Starts 
	EditMenu = Menu(MenuBar,tearoff = 0)

	# Give a feature of cut,copy,paste
	EditMenu.add_command(label = "Cut",command = cut)
	EditMenu.add_command(label = "Copy",command = copy)
	EditMenu.add_command(label = "Paste",command = paste)

	MenuBar.add_cascade(label = "Edit",menu = EditMenu)
	#Edit Menu Ends

	#Help menu Starts
	HelpMenu = Menu(MenuBar,tearoff = 0)
	HelpMenu.add_command(label = "About",command = about)
	MenuBar.add_cascade(label = "Help", menu = HelpMenu)
	#Help menu Ends 

	root.config(menu = MenuBar)

	# Adding Scrollbar 
	Scroll = Scrollbar(TextArea)
	Scroll.pack(side = RIGHT,fill = Y)
	Scroll.config(command = TextArea.yview)
	TextArea.config(yscrollcommand = Scroll.set)

	# Right click
	rightclick = Menu(root,tearoff = 0)
	rightclick.add_command(label = "Copy",command = copy)
	rightclick.add_command(label = "Cut",command = cut)
	rightclick.add_command(label = "Paste",command = paste)

	root.bind("<Button-3>",rightClickFun)


	root.mainloop()
