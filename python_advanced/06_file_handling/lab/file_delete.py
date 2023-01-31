import os
# abs_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(abs_path, "my_first_file.txt")
#
# if os.path.exists(file_path):
# 	os.remove('my_first_file.txt')
# else:
# 	print('File already deleted!')

try:
	os.remove('my_first_file.txt')
except FileNotFoundError:
	print("File already deleted!")