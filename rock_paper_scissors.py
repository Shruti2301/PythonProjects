import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']  # Make all lowercase for comparison

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()

    if user_input == 'q':
        print("Goodbye!")
        print(f"You won {user_wins} time(s).")
        print(f"The computer won {computer_wins} time(s).")
        break  # exit the loop instead of quit() to allow cleanup

    if user_input not in options:
        print("Invalid input. Try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print('Computer picked', computer_pick + '.')

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("You lost!")
        computer_wins += 1
