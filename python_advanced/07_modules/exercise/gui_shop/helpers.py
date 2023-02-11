from canvas import root


def clean_screen():
	for el in root.winfo_children():
		el.destroy()



	
