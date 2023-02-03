import os


def get_filenames_in_dict(dir_name='.'):
	data = {}
	
	cur_dir_files = os.listdir(dir_name)
	for file in cur_dir_files:
		file_name = os.path.join(dir_name, file)
		print(file_name)
		if os.path.isfile(file_name):
			file_extension = file[file.index('.'):]
			
			if file_extension not in data:
				data[file_extension] = []
			data[file_extension].append(file)
		elif os.path.isdir(file_name):
			get_filenames_in_dict(file_name)
	return data


# def write_filenames_to_file(data, filename='report.txt'):
# 	with open(filename, 'w') as file:
#
# 		for key, values in sorted(data.items()):
# 			file.writelines(f"{key}\n")
#
# 			for value in sorted(values):
# 				file.writelines(f"- - - {value}\n")


if __name__ == '__main__':
	file_data = get_filenames_in_dict(r'../../02_tuples_and_sets')
	print(file_data)
	# write_filenames_to_file(file_data)
