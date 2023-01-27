from functools import reduce


def fill_the_box(*args):
	box_size = reduce(lambda x, y: int(x) * int(y), args[:3])
	left_cubes = 0
	cubes_in_box = 0
	
	for arg in args[3:]:
		if arg == "Finish":
			break
		else:
			cubes_in_box += int(arg)
			
			if cubes_in_box > box_size:
				left_cubes += (cubes_in_box - box_size)
				cubes_in_box = box_size

	if box_size == cubes_in_box:
		return f"No more free space! You have {left_cubes} more cubes."
	return f"There is free space in the box. You could put {box_size - cubes_in_box} more cubes."
