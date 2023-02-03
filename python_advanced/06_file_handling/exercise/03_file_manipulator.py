import os


def create_file(filename):
	with open(filename[0], "w") as new_file:
		new_file.write('')


def append_to_file(info):
	filename, text = info[0], info[1]
	
	if os.path.exists(filename):
		with open(filename, "a") as current_file:
			current_file.writelines(f"{text}\n")
			
	else:
		with open(filename, "w") as current_file:
			current_file.writelines(f"{text}\n")


def replace_text_in_file(info):
	filename, old_text, new_text = info[0], info[1], info[2]
	
	if os.path.exists(filename):
		with open(filename, "r") as current_file:
			text = current_file.read()
			
		with open(filename, 'w') as current_file:
			current_file.write(text.replace(old_text, new_text))
			
	else:
		print("An error occurred")
		

def delete_file(filename):
	
	if os.path.exists(filename[0]):
		os.remove(filename[0])
	else:
		print("An error occurred")
		

data = {
	"Create": create_file,
	"Add": append_to_file,
	"Replace": replace_text_in_file,
	"Delete": delete_file,
}

command = input()
while command != "End":
	action, *file_data = command.split('-')
	
	data[action](file_data)
	
	command = input()
	