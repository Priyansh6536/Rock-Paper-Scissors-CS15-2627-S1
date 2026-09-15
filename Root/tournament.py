import random

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid answer. Please enter rock, paper, or scissors")

def check_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "Tie"
    elif cpu_choice == "rock":
        if player_choice == "scissors":
            return "CPU wins"
        else:
            return "Player wins"
    elif cpu_choice == "paper":
        if player_choice == "rock":
            return "CPU wins"
        else:
            return "Player wins"
    elif cpu_choice == "scissors":
        if player_choice == "paper":
            return "CPU wins"
        else:
            return "Player wins"

def play_round():
    cpu = get_cpu_choice()
    player = get_player_choice()

    print(f"\nYou chose: {player}")
    print(f"CPU chose: {cpu}")


    winner = check_winner(player, cpu)
    return winner

def score_keeping():
    player_wins = 0
    cpu_wins = 0
    ties = 0

    print(" First to 3 points wins ")
    while player_wins < 3 and cpu_wins < 3:
        winner = play_round()
        if winner == "CPU wins":
            cpu_wins += 1
            print("You lose this round!")
        elif winner == "Player wins":
            player_wins += 1
            print("You win this round!")
        else:
            ties += 1
            print("This round is a tie!")


        print(f"Scores: Player = {player_wins} CPU = {cpu_wins} Ties = {ties}")



    if player_wins == 3:
        print("You win the tournament!")
    else:
        print("CPU wins the tournament!")


score_keeping()