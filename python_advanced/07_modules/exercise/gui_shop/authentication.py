from tkinter import messagebox
from main import login_to_shop
from json import dump, load
from re import match as re_match


def login(username, password):
	with open('db/users.json', 'r') as file:
		user_data = load(file)
		
		for user, credentials in user_data.items():
			print(user)
			if user[0] == username and credentials['password'] == password:
				print('Login successful')
				login_to_shop()
				return
		else:
			messagebox.showinfo(message="Incorrect username or password.\nAre you sure you are registered?")
			return False


def valid_username(*args):
	error_msg = args[0]
	match = re_match(r"^[a-zA-Z0-9\-\_]{5,}$", args[1])

	if match:
		error_msg.set('')
		return True
	error_msg.set('Username must be at least 5 characters long and\n'
	              ' contain only numbers characters and dashes.')
	return False


def valid_password(*args):
	error_msg = args[0]
	match = re_match(r"([a-z0-9_A-Z@#$%^&+=]){8,}", args[1])

	if match:
		error_msg.set('')
		return True
	error_msg.set('Password must be at least 8 characters long and \n'
	              'can contain digits, letter and special characters')
	return False


def validate_registration(username, password, first_name, last_name, msg):
	if valid_username(msg, username) and valid_password(msg, password):
		register_(username, password, first_name, last_name, msg)


def register_(username, password, first_name, last_name, msg):
	with open('db/users.json', 'r') as file:
		user_data = load(file)
		for user in user_data:
			if user[0] == username:
				# messagebox.showinfo(message="Username already exists.")
				msg.set('Username already exists.')
				return False
		else:
			
			with open("db/users.json", 'r') as info:
				info_data = load(info)
				
			with open('db/users.json', 'w') as users:
				curr_user = {username: {'password': password, 'first Name': first_name,  'last Name': last_name}}
				# user_data = json.dump(curr_user, users)
				info_data |= curr_user
				dump(info_data, users)
				messagebox.showinfo(message='Registration successful.')
				# msg.set('Registration successful.')
				return True
