import random





def get_cpu_choice():
    choices = ["Rock", "Paper", "Scissors"]
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



cpu_choice = get_cpu_choice()

player_choice = get_player_choice()

winner = check_winner(cpu_choice, player_choice)

print(winner)





