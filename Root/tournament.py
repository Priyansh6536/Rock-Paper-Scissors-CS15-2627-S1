import random







def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(choices)
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ")
        player_choice = player_choice.lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid answer. Please enter rock, paper, or scissors")
def check_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "Tie"
    elif cpu_choice == "rock":
        if player_choice == "scissors":
            return "CPU"
        else:
            return "Player"
    elif cpu_choice == "paper":
        if player_choice == "rock":
            return "CPU"
        else:
            return "Player"
    elif cpu_choice == "scissors":
        if player_choice == "paper":
            return "CPU"
        else:
            return "Player"






def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(player_choice, cpu_choice)
    if winner == "CPU":

        print(f"The winner of this round is the {winner}")
    elif winner == "Player":

        print(f"The winner of this round is the {winner}")
    elif winner == "Tie":

        print("This round is a tie")
    return winner


player_wins = 0
cpu_wins = 0
tie = 0

print("Rock, Paper, or Scissors tournenent first to 3 wins")

while True:
    if player_wins < 3:
        if cpu_wins < 3:
            winner = play_round()
            if winner == "CPU":

                cpu_wins += 1
            elif winner == "Player":

                player_wins += 1
            elif winner == "Tie":
                tie += 1
        else:
            print("The CPU won the tournament")
            break
        print(f"Player wins: {player_wins}")
        print(f"CPU wins: {cpu_wins}")
        print(f"Ties: {tie}")
    else:
        print("You won the tournament")
        break

