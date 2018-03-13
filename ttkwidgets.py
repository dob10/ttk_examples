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

def selectWidget(*args):
	return

class App:
	def __init__(self, master):
		print("App.__init__(master)")
		self.mainframe = ttk.Frame(master, padding=(5))
		self.mainframe.pack()

		self.wnames = StringVar(value=widgetNames)

		self.widgetlist = Listbox(self.mainframe, listvariable=self.wnames, height=20)
		self.widgetlist.grid(column=0, row=0)

		self.widgetframe = ttk.Frame(self.mainframe, padding=(10), borderwidth=2, relief="sunken")
		self.widgetframe.grid(column=1, row=0, columnspan=3)

		self.testlabel = ttk.Label(self.widgetframe, text="This is a test label.")
		self.testlabel.grid(column=0, row=0)


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