import random
from art import logo

print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == "easy":
  print("You have 10 attempts remaining to guess the number.")
  attempts = 10
elif difficulty == "hard":
  print("You have 5 attempts remaining to guess the number.")
  attempts = 5
  
number = random.randint(1,100)
guess = int(input("Make a guess: "))

def check_guess(n_number,n_guess):
  if n_guess == n_number:
    print("You guessed the number!")
    return("You guessed the number!")
    print(f"The number was {n_number}")
  elif n_guess < n_number:
    print("Too low.")
    return("low")
  elif n_guess > n_number:
    print("Too high.")
    return("high")
    
flag = ""  

while attempts >= 1 and flag != "guessed":
  flag = check_guess(number,guess)
  #check_guess(number,guess)
  attempts -= 1
  print(f"You have {attempts} attempts remain.")
  if attempts >= 1:
    guess = int(input("Make a guess: "))