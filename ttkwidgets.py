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
		self.mainframe = ttk.Frame(master, padding=(5))
		self.mainframe.pack()

		# Create left side and right side of overall window
		self.wnames = StringVar(value=widgetNames)

		self.widgetlist = Listbox(self.mainframe, listvariable=self.wnames, height=20)
		self.widgetlist.grid(column=0, row=0)

		self.widgetframe = ttk.Frame(self.mainframe, padding=(10), width="250px")
		self.widgetframe.grid(column=1, row=0, columnspan=3)

		self.selected_widget = None

		# Bind Listbox options to change the example widget
		self.widgetlist.bind("<<ListboxSelect>>", self.switchExample)

	def switchExample(self, event):
		old_widget = self.selected_widget

		index = self.widgetlist.curselection()
		try:
			widgname = self.widgetlist.get(index)
			if widgname == "Button":
				self.showButton()
			elif widgname == "Checkbutton":
				self.showCheckbutton()
			elif widgname == "Entry":
				self.showEntry()
			elif widgname == "Frame":
				self.showFrame()

			if old_widget is not None:
				old_widget.destroy()
			self.selected_widget.grid(column=0, row=0)
		except:
			raise
		return

	def showButton(self):
		options = { "text":"Button" }
		self.selected_widget = ttk.Button(self.widgetframe, **options)

	def showCheckbutton(self):
		options = { "text":"Checkbutton" }
		# v = IntVar()
		self.selected_widget = ttk.Checkbutton(self.widgetframe, **options)
		self.selected_widget.invoke() # toggles into "on" state
		self.selected_widget.invoke() # toggles into "off" state

	def showEntry(self):
		entry_string = StringVar()
		options = { "textvariable":entry_string }
		self.selected_widget = ttk.Entry(self.widgetframe, **options)

	def showFrame(self):
		options = { "borderwidth":2,
					"relief":"sunken",
					"width":"250px",
					"height":"150px"
					}
		self.selected_widget = ttk.Frame(self.widgetframe, **options)

	def showLabel(self):
		pass

	def showLabelframe(self):
		pass

	def showMenubutton(self):
		pass

	def showPanedWindow(self):
		pass

	def showRadiobutton(self):
		pass

	def showScale(self):
		pass

	def showScrollbar(self):
		pass

	def showCombobox(self):
		pass

	def showNotebook(self):
		pass

	def showProgressbar(self):
		pass

	def showSeparator(self):
		pass

	def showSizegrip(self):
		pass

	def showTreeview(self):
		pass

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
