left = []
middle = []
right = []

def create_towers(num_disks):
	for i in range(num_disks, 0, -1):
		left.append(i)

def get_num_disks():
	return int(input("How many disks do you want to play with?\n"))

def get_user_input():
	while True:
		print("Enter 'L' for Left")
		print("Enter 'M' for Middle")
		print("Enter 'R' for Right")
		user_choice = input("\nPut choice here: ")
		if user_choice == 'L':
			return left
		elif user_choice == 'M':
			return middle
		elif user_choice == 'R':
			return right
		else:
			print("\nThat isn't valid choice. Try again.\n")

	

def print_towers():
	print("\nCurrent Towers....\n")
	print("Left: {0}".format(left))
	print("Middle: {0}".format(middle))
	print("Right: {0}".format(right))

def is_valid_move(from_tower, to_tower):
	if not from_tower:
		return False
	else:
		if not to_tower:
			return True
		elif from_tower[len(from_tower) - 1] > to_tower[len(to_tower) - 1]:
			return False
		else:
			return True

def is_solved(num_disks):
	if len(right) != num_disks:
		return False
	return True

def play_game():
	num_disks = get_num_disks()
	create_towers(num_disks)
	while not is_solved(num_disks):
		print_towers()
		while True:
			print("\nWhat tower do you want to move from?\n")
			from_tower = get_user_input()
			print("\nWhat tower do you want to move to?\n")
			to_tower = get_user_input()
			if is_valid_move(from_tower, to_tower):
				to_tower.append(from_tower.pop())
				break
			else:
				print("\nThat isn't a valid move. Try again.\n")
				print_towers()
	print_towers()
	print("\nCongrats! You solved Towers of Hanoi!!")

if __name__ == "__main__": play_game()





	

