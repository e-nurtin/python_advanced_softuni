import os
import re

dir_name = input("Enter a directory: ")
string_to_replace = input("String to replace: ")
replacement_string = input("Replacement string: ")

for filename in os.listdir(dir_name):
	file_path = os.path.join(dir_name, filename)
	
	if os.path.isfile(file_path):
		new_name = filename.replace(string_to_replace, replacement_string, 1)
		new_file = '/'.join(re.split(r"[/\\]", file_path)[:-1]) + '/' + new_name
		os.rename(os.path.join(dir_name, filename), new_file)
