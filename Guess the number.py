import random

def guess_number():
    lower_bound = 1
    upper_bound = 50
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to the Guess the Number game! Try to guess the number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

if __name__ == "__main__":
    guess_number()
