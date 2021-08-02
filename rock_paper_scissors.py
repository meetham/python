
import random

rps=["Scissors","Rock","Paper"]
computer_choice=random.choice(rps)
ppl_choice=input(" Enter 'Rock', 'Paper', or 'Scissors'\n")

if ppl_choice == computer_choice:
    print("Try again! a Tie\n")
elif ppl_choice=="Paper" and computer_choice=="Rock":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You win!\n")
elif ppl_choice=="Paper" and computer_choice=="Scissors":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You lose!\n")
elif ppl_choice=="Rock" and computer_choice=="Paper":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You lose!\n")
elif ppl_choice=="Rock" and computer_choice=="Scissors":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You win!\n")
elif ppl_choice=="Scissors" and computer_choice=="Paper":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You win!\n")
elif ppl_choice=="Scissors" and computer_choice=="Rock":
    print("Computer chose "+computer_choice +". You chose "+ppl_choice +". You lose!\n")
else:
    print("Unknown Input\n")
