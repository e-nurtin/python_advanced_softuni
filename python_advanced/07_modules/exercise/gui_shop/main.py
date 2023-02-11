from canvas import root, frame
from authentication import *
from helpers import clean_screen
from tkinter import ttk, Button
from tkinter import StringVar
from PIL import ImageTk, Image
from json import load, dump


def main_screen():
	content = frame()
	label = ttk.Label(content, text='Welcome to the shop please log in or register to continue!')
	label.grid(row=0, column=1, columnspan=3)
	button_login = ttk.Button(content, text='Login', command=login_page)
	button_login.grid(row=1, column=1)
	button_register = ttk.Button(content, text='Register', command=register_page)
	button_register.grid(row=1, column=2)


def login_page(*args):
	clean_screen()
	content = frame()
	username = ttk.Entry(content)
	password = ttk.Entry(content, show='•')
	
	button_login = ttk.Button(content, text='Login', command=lambda: login(username.get(), password.get()))
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
	
	error_message = StringVar()
	error_lbl = ttk.Label(content, textvariable=error_message, foreground='red')
	error_lbl.grid(row=11, column=0, columnspan=2)
	
	user_check = (content.register(lambda x: valid_username(error_message, x)), '%P')
	username = ttk.Entry(content, validate='focusout', validatecommand=user_check)
	
	ttk.Label(content, text='Username:').grid(row=1, column=0)
	
	pass_check = (content.register(lambda x: valid_password(error_message, x)), '%P')
	password = ttk.Entry(content, show='•', validate='focusout', validatecommand=pass_check)
	ttk.Label(content, text='Password:').grid(row=2, column=0)
	
	first_name = ttk.Entry(content)
	ttk.Label(content, text='First Name:').grid(row=3, column=0)
	
	last_name = ttk.Entry(content)
	ttk.Label(content, text='Last Name:').grid(row=4, column=0)
	
	username.grid(row=1, column=1, columnspan=2)
	password.grid(row=2, column=1, columnspan=2)
	first_name.grid(row=3, column=1, columnspan=2)
	last_name.grid(row=4, column=1, columnspan=2)
	
	button_back = ttk.Button(content, text='Back', command=main_screen)
	button_register = ttk.Button(
		content,
		text='Register',
		default='active',
		command=lambda: validate_registration(username.get(),
		                                      password.get(),
		                                      first_name.get(),
		                                      last_name.get(),
		                                      error_message)
	)
	button_register.grid(row=6, column=0)
	button_back.grid(row=6, column=1)


def login_to_shop():
	clean_screen()
	shop_page()


def shop_page(*args):
	content = frame()
	
	row, col = 0, 0
	with open('products/products.json', 'r') as file:
		
		products = load(file)
		
		for product in products.items():
			photo_img = Image.open(product[1]['img_path']).resize((200, 200))
			
			img = ImageTk.PhotoImage(photo_img)
			label = ttk.Label(content, image=img, text='apple', padding='5')
			ttk.Label(content, text=f'{product[0]}').grid(row=row + 1, column=col)
			state = 'normal' if product[1]['count'] > 0 else 'disabled'
			ttk.Label(
				content,
				text=f"Availability: {product[1]['count'] if product[1]['count'] > 0 else 'Out of Stock'}"
			).grid(row=row + 2, column=col)
			
			buy_btn = Button \
							(
							content,
							text='Buy', bg=f"{'green' if product[1]['count'] > 0 else 'red'}",
							fg='white',
							state='disabled',
							command=lambda x=product: buy_product(x, products)
						)
					
			buy_btn.grid(row=row + 3, column=col)
			buy_btn['state'] = state
			
			label.image = img
			label.grid(row=row, column=col)
			
			col += 1
			
			if col == 3:
				col = 0
				row += 4


def buy_product(product, info):
	info[product[0]]['count'] -= 1
	with open('products/products.json', 'w') as file:
		dump(info, file, indent=2)
	login_to_shop()


if __name__ == '__main__':
	main_screen()
	root.mainloop()
