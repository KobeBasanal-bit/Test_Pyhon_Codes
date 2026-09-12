import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
guess = int(input("Take a guess: "))

if guess == secret_number:
    print("Spot on! You guessed it.")
else:
    print(f"Not quite! The number was {secret_number}.")