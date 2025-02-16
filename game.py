import random
import os

choices_list = ('rock','paper','scissors')

player_score = 0
computer_score = 0


def who_wins():
    global player_score
    global computer_score
    if user_choice == computer_choice:
        print("You tied!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("you win!")
        player_score = player_score + 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("you win!")
        player_score = player_score + 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("you win!")
        player_score += 1
    else:
        print("you lose!")
        computer_score += 1

def total_matches():
    global computer_score
    global player_score
    if player_score > computer_score:
        os.system("clear")
        print(f"you won the most matches!\nYour Score: {player_score}\nComputer Score: {computer_score}\nWon By: {player_score - computer_score}")
        exit()
    elif player_score < computer_score:
        os.system("clear")
        print(f"you lost the most matches!\nYour Score: {player_score}\nComputer Score: {computer_score}\nBeat By: {computer_score - player_score}")
        exit()
    else:
        exit()
        

while True:
    print(f"Your Score: {player_score}\nComputer Score {computer_score} ")
    user_choice = input("Enter a Choice rock, paper, scissors, q to quit: ").lower()
    if user_choice == "q":
        total_matches()
        break
    if user_choice not in choices_list:
        print("invaild choice")
        continue
    else:
        computer_choice = random.choice(choices_list)
        print(f"you chose {user_choice} and computer chose {computer_choice}")
        who_wins()
