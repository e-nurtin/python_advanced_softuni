from canvas import root


def clean_screen():
	for el in root.grid_slaves():
		el.destroy()
