import random

def guessing_game():
    
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("I have picked a secret number between 1 and 20. Try to guess it!")

    
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1 
        
        if user_guess < secret_number:
            print("Too low! Try a higher number.")
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break 
guessing_game()
