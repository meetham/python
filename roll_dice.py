import random

roll=random.randint(1,6)
guess=int(input("Guess the dice roll:\n:"))
result= "You guessed incorrectly :("
if roll==guess:
    result="You guessed correctly!"
print("The computer rolled a " + str(roll) + ". You guessed "5
 +  str(guess)+ " .\n" + result+"\n ")