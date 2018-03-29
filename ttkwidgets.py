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
			elif widgname == "Label":
				self.showLabel()
			elif widgname == "Labelframe":
				self.showLabelframe()
			elif widgname == "Menubutton":
				self.showMenubutton()
			elif widgname == "PanedWindow":
				self.showPanedWindow()
			elif widgname == "Radiobutton":
				self.showRadiobutton()
			elif widgname == "Scale":
				self.showScale()
			elif widgname == "Scrollbar":
				self.showScrollbar()
			elif widgname == "Combobox":
				self.showCombobox()
			elif widgname == "Notebook":
				self.showNotebook()
			elif widgname == "Progressbar":
				self.showProgressbar()
			elif widgname == "Separator":
				self.showSeparator()
			elif widgname == "Sizegrip":
				self.showSizegrip()
			elif widgname == "Treeview":
				self.showTreeview()

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
		options = { "text":"This is a Label" }
		self.selected_widget = ttk.Label(self.widgetframe, **options)

	def showLabelframe(self):
		options = { "text":"This is a Labelframe",
					"width": "250px",
					"height": "150px",
					"borderwidth":2 }
		self.selected_widget = ttk.Labelframe(self.widgetframe, **options)

	def showMenubutton(self):
		options = {"text": "Menubutton"}
		self.selected_widget = ttk.Menubutton(self.widgetframe, **options)

		# self.selected_widget.menu = Menu(self.selected_widget, tearoff=0)
		menu = Menu(self.selected_widget, tearoff=0)
		self.selected_widget["menu"] = menu
		menu.add_cascade(label="option1")
		menu.add_cascade(label="option2")
		menu.add_separator()
		menu.add_checkbutton(label="checkbutton")
		menu.add_command(label="command")
		menu.add_radiobutton(label="radiobutton")

	def showPanedWindow(self):
		options = { "height":250,
					"width": 450,
					"orient":VERTICAL}
		self.selected_widget = ttk.PanedWindow(self.widgetframe, **options)
		f1 = ttk.Labelframe(self.selected_widget, text="pane1", width=100, height=100)
		f2 = ttk.Labelframe(self.selected_widget, text="pane2", width=100, height=100)

		self.selected_widget.add(f1)
		self.selected_widget.add(f2)

	def showRadiobutton(self):
		rbframe = ttk.Frame(self.widgetframe)
		ctrlvar = IntVar()
		options = { "text": "option1",
					"variable": ctrlvar,
					"value": 0 }
		rb1 = ttk.Radiobutton(rbframe, **options)
		rb2 = ttk.Radiobutton(rbframe, text="option2", variable=ctrlvar, value=1)
		rb3 = ttk.Radiobutton(rbframe, text="option3", variable=ctrlvar, value=2)

		rb1.grid(row=0, column=0)
		rb2.grid(row=1, column=0)
		rb3.grid(row=2, column=0)


		self.selected_widget = rbframe

	def showScale(self):
		ctrlvar = DoubleVar()
		options = { "orient": HORIZONTAL,
					"from_":0.0,
					"to": 10.0,
					"value": 5.0,
					"variable": ctrlvar}
		scl = ttk.Scale(self.widgetframe, **options)

		self.selected_widget = scl

	def showScrollbar(self):
		options = { "orient": VERTICAL }
		scrllbar = ttk.Scrollbar(self.widgetframe, **options)

		self.selected_widget = scrllbar

	def showCombobox(self):
		str_var = StringVar()
		options = { "textvariable": str_var }
		cbox = ttk.Combobox(self.widgetframe, **options)

		self.selected_widget = cbox

	def showNotebook(self):
		options = { "width": 250}
		notebook = ttk.Notebook(self.widgetframe, **options)
		f1 = ttk.Frame(notebook)
		f2 = ttk.Frame(notebook)
		f3 = ttk.Frame(notebook)
		notebook.add(f1, text="one")
		notebook.add(f2, text="two")
		notebook.add(f3, text="three")

		self.selected_widget = notebook

	def showProgressbar(self):
		ctrlvar = DoubleVar()
		options = { "mode": "determinate",	# can also be "indeterminate"
					"orient": HORIZONTAL,
					"length": 200,
					"maximum": 100,
					"variable": ctrlvar }
		pbar = ttk.Progressbar(self.widgetframe, **options)
		pbar.start()

		self.selected_widget = pbar

	def showSeparator(self):
		mf = ttk.Frame(self.widgetframe)
		f1 = ttk.Label(mf, text="Label 1")


		options = { "orient": HORIZONTAL }
		sep = ttk.Separator(mf, **options)
		f2 = ttk.Label(mf, text="Label 2")

		f1.grid(row=0)
		sep.grid(row=1, sticky="ew") # Important: sticky is what makes the seperator go from edge to edge
		f2.grid(row=2)

		self.selected_widget = mf

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
