Title = '------GAMES------'
print("*"*len(Title))
print(Title)
print("*"*len(Title))
print("Please enter your details in order to play the games")

user_db = {"abhiram":["abhiram45","abhi@5544.co.uk"]}
global username

option=input("""
Menu:
1.Register
2.Login

select an option: """)

while option == '1':
	print("\n Register")

	while True:
		reg_user=input("\n enter the username: ")

		if(reg_user in user_db):
			print("\n username already exist")
		elif len(reg_user)<4 or len(reg_user)>20:
			print("\n username must be between 4-20 characters")
		elif reg_user[0].isalpha()!=True:
			print('\n username must start with letter')
		elif reg_user.isalnum() == False:
			print("\n username can only contain numbers and letters")
		else:
			break

	while True:
		reg_pass = input("\n Enter password: ")

		if len(reg_pass) < 6:
			print("password must be greater than 6 letters")
		elif reg_pass.isdigit() == True or reg_pass.isalpha() == True:
			print("password must not contain numbers and letters")
		else:
			break
	while True:
		reg_email = input("enter the email of the username:")
		reg_email = reg_email.lower()

		for lists in user_db.values():
			if lists[1] == reg_email:
				print('email address already exist')
			elif reg_email.count('@')!=1 or reg_email.count(".") == 0 or len(reg_email)<10:
				 print("invalid email_address")
				 break
		else:
			break
	

	

	print(f"{reg_user} you may login")
	
	break
	


while option == '2':
	while True:
		username=input("enter username: ")

		if username not in user_db:
			print("no such username1")
		else:
			break

	while True:
			password = input("Enter password: ")

			if password != user_db[username][0]:
				print("incorrect password!")
			else:
				break
	

	print(f"welcome {username}")
	break

print('Have a great fun by playing  the games')
print('-----PLAY THE FIRST GAME -----')

score = 1

def u_input():
		global user_input
		print(f"player score is {score}")
		user_input = input("player scored : ")

def player_move():
		if user_input in ('1','one'):
			return '1'
		elif user_input in ('2','two'):
			return '2'
		elif user_input in ('3','three'):
			return '3'
		elif user_input in ('4','four'):
			return '4'
		elif user_input in ('5','five'):
			return '5'
		elif user_input in ('6','six'):
			return '6'
		else :
			return False

def computer_move():
		import random
		number = ('1','2','3','4','5','6')
		comp = random.choice(number)
		return comp

def check_winner():
		global score
		player = player_move()
		computer = computer_move()

		if player == False:
			print("enter the numbers")
		elif player == '1' and computer == '1' :
			print("you: " ,player)
			print("computer:", computer)
			print('player is out')
			score = 0
		elif player == '2' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '3' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '4' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '5' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")
		elif player == '6' and computer == '1':
			score +=1
			print("you: " ,player)
			print("computer:", computer)
			print("play the game")

		elif player == '1' and computer == '2' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score +=1
		elif player == '2' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '3' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '2':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '3' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score +=1
		elif player == '2' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '4' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '3':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '4' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '5' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '4':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '5' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		elif player == '6' and computer == '5':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")

		elif player == '1' and computer == '6' :
			print("you: " ,player)
			print("computer:", computer)
			print('play the game')
			score += 1
		elif player == '2' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '3' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '4' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '5' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score +=1
			print("play the game")
		elif player == '6' and computer == '6':
			print("you: " ,player)
			print("computer:", computer)
			score = 0
			print("player is out")
		else :
			print(end)

title = """ *** Cricket *** """
print('*'*len(title))
print(title)
print('*'*len(title))
print('The initial socre of the player is "1"')

while score > 0 :
	u_input()
	player_move()
	computer_move()
	check_winner()

print("YOUR FIRST GAME IS COMPLETED")
print("PLAY THE SECOND GAME")

print("you can play second game until your money is completed")

money = 15

def balance():
		global user_input
		print(f"you have {money}")
		print("it's $5 to play")
		user_input = input("pick rock,paper,scissor: ")

def player_move():
		if user_input in ("ROCK","rock","r","R"):
			return "rock"
		elif user_input in ("PAPER",'P','paper','p'):
			return "paper"
		elif user_input in ("SCISSOR",'S','scissor','s'):
			return "scissor"
		else :
			return False

def computer_move():
		import random
		rps = ("rock","paper","scissor")
		comp = random.choice(rps)
		return comp

def check_winner():
		global money
		player = player_move()
		computer = computer_move()

		if player == False:
			print("please pick rock ,paper,scissor")
			
		elif player == "rock" and computer == "rock":
			print('\n you:' ,player)
			print('\n computer: ', computer, '\n its a draw.\n')
		elif player == "scissor" and computer == "rock":
			print("\n you: " ,player)
			print("\n computer:", computer,"\n computer wins.\n")
			money -= 5
		elif player =="paper" and computer == "rock":
			print("\n you:", player)
			print('\n computer:',computer,"\n player wins.\n")
			money += 5

		elif player == "paper" and computer == "paper":
			print('\n you:' ,player)
			print('\n computer: ', computer, '\n its a draw.\n')
		elif player == "rock" and computer == "paper":
			print("\n you: " ,player)
			print("\n computer:", computer,"\n computer wins.\n")
			money -= 5
		elif player =="scissor" and computer == "paper":
			print("\n you:", player)
			print('\n computer:',computer,"\n player wins.\n")
			money += 5

		elif player == "scissor" and computer == "scissor":
			print('\n you:' ,player)
			print('\n computer: ', computer, '\n its a draw.\n')
		elif player == "paper" and computer == "scissor":
			print("\n you: " ,player)
			print("\n computer:", computer,"\n computer wins.\n")
			money -= 5
		elif player =="rock" and computer == "scissor":
			print("\n you:", player)
			print('\n computer:',computer,"\n player wins.\n")
			money += 5

		
title = " *** Rock-Paper-Scissors ***"
print("-"*len(title))
print(title)		
print("-"*len(title))


while money > 0:
	balance()
	player_move()
	computer_move()
	check_winner()


print("you don't have any money left")

