import random

top_of_range = input("Type a number: ")

# Validate input is a positive integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate random number between 0 and top_of_range (inclusive)
random_number = random.randint(0, top_of_range)

# Initialize guess counter
guesses = 0

# Guessing loop
while True:
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1  # Count only valid guesses

        if user_guess <= 0:
            print("Please type a number larger than 0.")
            continue

        if user_guess == random_number:
            print("Correct! You guessed the number.")
            break  # Exit the loop
        elif user_guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print("Please enter a valid number.")

# Show total number of guesses
print("You got it in", guesses, "guess(es).")
