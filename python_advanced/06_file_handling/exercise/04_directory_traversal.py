import os


def get_filenames_in_dict(dir_name='.'):
	data = {}
	
	cur_dir_files = os.listdir(dir_name)
	for file in cur_dir_files:
		file_name = os.path.join(dir_name, file)

		if os.path.isfile(file_name):
			file_extension = file[file.index('.'):]
		
			if file_extension not in data:
				data[file_extension] = []
				
			data[file_extension].append(file)

	return data


def write_filenames_to_file(data, filename='report.txt'):
	with open(filename, 'w') as file:

		for key, values in sorted(data.items()):
			file.writelines(f"{key}\n")

			for value in sorted(values):
				file.writelines(f"- - - {value}\n")


file_data = get_filenames_in_dict()

write_filenames_to_file(file_data)
