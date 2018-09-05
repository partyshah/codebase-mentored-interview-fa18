left = []
middle = []
right = []

def create_towers(num_disks):
    #Replace and Fill In Code Here
    pass

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
    #Replace and Fill In Code Here
    pass

def is_solved(num_disks):
    #Replace and Fill In Code Here
    pass

def play_game():
    num_disks = get_num_disks()
    create_towers(num_disks)
    #Fill In Code Here

if __name__ == "__main__": play_game()
