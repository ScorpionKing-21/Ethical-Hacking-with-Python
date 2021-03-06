from pynput.mouse import Controller
from pynput.mouse import Listener
from pynput.keyboard import Controller
from pynput.keyboard import Listener
import sys
import time


def pyK():
	print('Welcome to the pyk Tool to capture keyboard and mouse inputs')
	print('1) To capture the key board input ')
	print('2) To move you mouse on screen based on x and y pixal position (Top left is your (0, 0) position ')
	print('3) To capture the mouse position ')
	func = input('Select Your Option? :- ')

	if func == '1':
		file_name = input('Specify the file name in which you would like to capture (For Example: default=capture.txt ')
		if not file_name:
			file_name = "captured_input.txt"
		print('the capture has been started...')
		def writeToFile(keys):
			letter = str(keys)
			letter = letter.replace("'", "")

			if letter == 'Key.space':
				letter = ' '
			if letter == 'Key.enter':
				letter = '\n'
			with open(file_name, mode='a') as file:
				file.write(letter)

		with Listener(on_press=writeToFile) as l:
			l.join()
	elif func == '2':
		import mouse
		x, y = input('Please specify the x nd y position (For example: 300 500)').split()
		def controlMouse(x, y):
			mouse = Controller()
			mouse.position = (x, y)
		controlMouse(x, y)
	elif func == '3':
		import livemouse
		print('The Capture has been started...')
		def mousemove(x, y):
			print(f"\rx-axis: "+ str(x), end="")
			print(f"\rY-axis: "+ str(y), end="")
		with Listener(on_move=mousemove) as l_mouse:
			l_mouse.join()
	else:
		print('Select a Valid Input >:) ')
		pyK()

if __name__ == '__main__':
	try:
		pyK()
	except KeyboardInterrupt:
		print('\nExiting...')