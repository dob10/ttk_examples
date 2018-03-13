#!/usr/bin/env python3

# -------
# imports
# -------

import sys
from tkinter import *
from tkinter import ttk
# -------
# declarations
# -------
widgetNames = ("Button", "Checkbutton", "Entry", "Frame", "Label", "Labelframe",
 		"Menubutton", "PanedWindow", "Radiobutton", "Scale", "Scrollbar", 
 		"Combobox", "Notebook", "Progressbar", "Separator", "Sizegrip", "Treeview")

class App:
	def __init__(self, master):
		print("App.__init__(master)")
		self.mainframe = ttk.Frame(master, padding=(5))
		self.mainframe.pack()

		# Create left side and right side of overall window
		self.wnames = StringVar(value=widgetNames)

		self.widgetlist = Listbox(self.mainframe, listvariable=self.wnames, height=20)
		self.widgetlist.grid(column=0, row=0)

		self.widgetframe = ttk.Frame(self.mainframe, padding=(10))
		self.widgetframe.grid(column=1, row=0, columnspan=3)

		self.testlabel = ttk.Label(self.widgetframe, text="This is a test label.")
		self.testlabel.grid(column=0, row=0)

		# Bind Listbox options to change the example widget
		self.widgetlist.bind("<<ListboxSelect>>", self.switchExample)

	def switchExample(self, event):
		print("In App.switchExample")
		index = self.widgetlist.curselection()
		newText = self.widgetlist.get(index) + " was selected."
		self.testlabel = ttk.Label(self.widgetframe, text=newText)
		self.testlabel.grid(column=0, row=0)
		return

######## End of App


"""
main
called if this script is the main program
"""
def my_main():
	root = Tk()
	root.title("ttk Widget Examples")

	app = App(root)

	root.mainloop()
	try:
		root.destroy()
	except:
		print("Window destroyed before destroy() method. Should be fine.")

	return

# -------
# main
# -------

if __name__ == "__main__":
	my_main()