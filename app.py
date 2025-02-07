import random

def guess_the_number():
    print("\nWelcome to the Guess the Number game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input(f"\nGuess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print("Out of range! Try again.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Rixi game! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts! 🎉")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_the_number()

