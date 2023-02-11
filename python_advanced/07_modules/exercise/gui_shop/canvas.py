from tkinter import *
from tkinter import ttk


def create_window():
	tk = Tk()
	tk.minsize(600, 300)
	tk.title("GUI Product Shop")
	
	return tk


def frame():
	content = ttk.Frame(root, padding=(3, 3, 12, 12), relief='sunken')
	content.grid(column=0, row=0, sticky=(N, S, E, W))
	content.rowconfigure(0, weight=1)
	content.columnconfigure(0, weight=1)
	
	return content


root = create_window()