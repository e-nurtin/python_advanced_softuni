from canvas import root
from tkinter import ttk, messagebox
from tkinter import *
from helpers import clean_screen
import json


def frame():
	content = ttk.Frame(root, padding=(3, 3, 12, 12), relief='sunken')
	content.grid(column=0, row=0, sticky=(N, S, E, W))
	content.rowconfigure(0, weight=1)
	content.columnconfigure(0, weight=1)
	return content


def main_screen():
	content = frame()
	label = ttk.Label(content, text='Welcome to the shop please log in or register to continue!')
	label.grid(row=0, column=1, columnspan=3, sticky=(N, S, E, W))
	button_login = ttk.Button(content, text='Login', command=login_page)
	button_login.grid(row=1, column=1, sticky=(N, S, E, W), )
	button_register = ttk.Button(content, text='Register', command=register_page)
	button_register.grid(row=1, column=2, sticky=(N, S, E, W))


def login_page(*args):
	clean_screen()
	content = frame()
	username = ttk.Entry(content)
	password = ttk.Entry(content, show='•')
	
	button_login = ttk.Button(content, text='Login', command=lambda: login_(username.get(), password.get()))
	button_back = ttk.Button(content, text='Back', command=main_screen)
	
	ttk.Label(content, text='Username:').grid(row=1, column=0)
	ttk.Label(content, text='Password:').grid(row=2, column=0)
	
	button_login.grid(row=4, column=0)
	button_back.grid(row=4, column=1)
	
	username.grid(row=1, column=1, columnspan=2)
	password.grid(row=2, column=1, columnspan=2)


def register_page(*args):
	clean_screen()
	content = frame()
	username = ttk.Entry(content)
	password = ttk.Entry(content, show='•')
	first_name = ttk.Entry(content)
	last_name = ttk.Entry(content)
	ttk.Label(content, text='Username:').grid(row=1, column=0)
	ttk.Label(content, text='Password:').grid(row=2, column=0)
	ttk.Label(content, text='First Name:').grid(row=3, column=0)
	ttk.Label(content, text='Last Name:').grid(row=4, column=0)
	
	username.grid(row=1, column=1, columnspan=2)
	password.grid(row=2, column=1, columnspan=2)
	first_name.grid(row=3, column=1, columnspan=2)
	last_name.grid(row=4, column=1, columnspan=2)
	
	button_back = ttk.Button(content, text='Back', command=main_screen)
	button_register = ttk.Button(content, text='Register',
	                             command=lambda: register_(username.get(), password.get(), first_name.get(),
	                                                       last_name.get()))
	button_register.grid(row=6, column=0)
	button_back.grid(row=6, column=1)


def login_(username, password):
	print(username, password)
	with open('db/user_credentials_db.txt', 'r') as file:
		lines = file.readlines()
		for line in lines:
			line = line[:-1].split(', ')
			
			if line[0] == username and line[1] == password:
				print('yes')
		else:
			messagebox.showinfo(message="Incorrect username or password.\nAre you sure you are registered?")
		# print("Incorrect username or password.\nAre you sure you are registered?")


def register_(username, password, first_name, last_name):
	print(username, password, first_name, last_name)
	with open('db/users.txt', 'a') as users:
		# json.dumps("[asd: {klmn: asd}")
		users.write(json.dumps({'Username': username, 'Password': password, 'First Name': first_name, 'Last Name': last_name}, indent=""))
	with open('db/user_credentials_db.txt', 'a') as credentials:
		credentials.write(f"{username}, {password}")
		