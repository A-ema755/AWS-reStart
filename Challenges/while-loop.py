import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

adivinaste = False

while adivinaste == False:
    # pedir nro a usuario
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        adivinaste = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


print("I guessed")