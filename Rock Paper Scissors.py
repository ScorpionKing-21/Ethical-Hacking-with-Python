print('Welcome to rock paper scissors game')
name = input('Please write your good name: ')
# user choice from rock paper and scissor #
def user_choice():
	choice = input('-- Choose between [r] for rock, [p] for paper, [s] for scissor --').lower()
	return choice
##
# computer choice #
import random
def comp_choice():
	ran = random.randint(1,3)
	if ran == 1:
		return 'r'
	elif ran == 2:
		return 'p'
	elif ran == 3:
		return 's'	
##
# who wins? #
def play_who_wins():
	computer = comp_choice()
	user = user_choice()

	if (computer == 'r' and user == 'p') or (computer == 'p' and user == 's') or (computer == 's' and user == 'r'):
		user = True
		computer = False
	elif (computer == 'p' and user == 'r') or (computer == 's' and user == 'p') or (computer == 'r' and user == 's') :
		computer = True
		user = False
	else:
		user = True
		computer = True

	return (user,computer)
##

# playing game again and again and to stop it #
def replay():
	return input('Do you want to play again [Y] for yes or [N] for not ').upper().startswith('Y')
##

# while loop to continuously run the game #
while True:
	play = input('Are you ready to play [Y] for yes [N] for no ').upper()
	play = play[0]
	if play == 'Y':
		game_start = True
	else:
		game_start = False

	while game_start:
		user,computer = play_who_wins()
		if user == True and computer == True:
			print('-----------------------------------------')
			print('Its a Tie')
			print('-----------------------------------------')
			break
		elif computer == True:
			print('-----------------------------------------')
			print('Sorry! '+name+' You lost')
			print('-----------------------------------------')
			break
		elif user == True:
			print('-----------------------------------------')
			print('Congrats! '+name+' You have won')
			print('-----------------------------------------')
			break	

	if not replay():
		break
##
print('Thanks for playing')
end = input('Press return to exit')