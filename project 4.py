number = 50
print("Welcome to the Guessing Game!")
print("Guess the number between 1 and 100.")
while True:
    guess = int(input("Enter your guess: "))
    if guess > number:
        print("Too high! Try again.")
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number!")
        break