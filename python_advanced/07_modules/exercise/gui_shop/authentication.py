from canvas import root
from tkinter import ttk
from tkinter import *
from helpers import clean_screen


def login_(username, password):
	with open('db/user_credentials_db.txt', 'r') as file:
		lines = file.readlines()
		pass
