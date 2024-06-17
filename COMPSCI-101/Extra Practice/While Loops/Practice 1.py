import random
guess = int(input("Guees a number between 1 and 100: "))
while guess < 1 or guess > 100:
    guess = int(input("Guess a number between 1 and 100:"))
number = random.randrange(1, 100, 1 )

while guess != number:
    if guess < number:
        print("Too Low")
        guess = int(input("Guess a number between 1 and 100:"))
    elif guess > number:
        print("Too High")
        guess = int(input("Guess a number between 1 and 100:"))
print(f"Your guess of {guess} is equal to the random number: {number}")


