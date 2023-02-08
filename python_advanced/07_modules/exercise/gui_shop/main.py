from canvas import root
from authentication import login_
from helpers import clean_screen
from tkinter import ttk
from tkinter import *


def frame():
	content = ttk.Frame(root, padding=(3, 3, 12, 12), relief='sunken')
	content.grid(column=0, row=0, sticky=(N, S, E, W))
	content.rowconfigure(0, weight=1)
	content.columnconfigure(0, weight=1)
	return content


def landing_page():
	content = frame()
	label = ttk.Label(content, text='Welcome to the shop please log in or register to continue!')
	label.grid(row=0, column=1, columnspan=3, sticky=(N, S, E, W))
	button_login = ttk.Button(content, text='Login', command=login_page)
	button_login.grid(row=1, column=1, sticky=(N, S, E, W), )
	button_register = ttk.Button(content, text='Register', command=clean_screen)
	button_register.grid(row=1, column=2, sticky=(N, S, E, W))


def login_page(*args):
	clean_screen()
	content = frame()
	username = ttk.Entry(content)
	password = ttk.Entry(content)
	
	button_login = ttk.Button(content, text='Login', command=lambda: login_(username.get(), password.get()))
	button_login.grid(row=4, column=0, columnspan=2)
	
	username.grid(row=2, column=1)
	password.grid(row=3, column=1)


if __name__ == '__main__':
	landing_page()
	root.mainloop()
