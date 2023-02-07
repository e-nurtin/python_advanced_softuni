from pyfiglet import figlet_format


def msg_art(msg):
	print(figlet_format(msg, font='smallbold'))
	

msg_art('Tic Tac Toe')