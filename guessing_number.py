# A guessing game for a random number between 1 and 100 (including)
# Two difficulties available, easy (10 attempts) or hard (5 attempts)

from random import randint


def play(difficulty_choice):
    """Plays the game"""
    answer = randint(1, 100)
    attempts = 10
    if difficulty_choice == "hard":
        attempts = 5
    while attempts > 0:
        print(f"\nYou have {attempts} attempts to guess the number.")
        guess = input("Make a guess: ")
        try:
            if int(guess) == answer:
                print("Your guess is correct!")
                return
            elif int(guess) > answer:
                print("Too high.")
                attempts -= 1
            else:
                print("Too low.")
                attempts -= 1
        except ValueError:
            print("Error: Guess only numbers.")
    print(f"\nYou lost. The correct number was {answer}")


print("Welcome to the Guessing Number Game!")
print("I'm guessing a number between 1 and 100.")
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        play(difficulty)
        break
    else:
        print("Error: invalid option.")
