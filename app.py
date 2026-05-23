import random

VALID_CHOICES = ["rock", "paper", "scissors"]
QUIT_OPTION = "quit"


def get_player_choice() -> str:
    """Prompt the player for a choice and validate the input."""
    while True:
        player_input = input("Choose rock, paper, scissors, or quit: ").strip().lower()
        if player_input == QUIT_OPTION:
            return player_input
        if player_input in VALID_CHOICES:
            return player_input
        print("Invalid option. Please enter rock, paper, scissors, or quit.")


def get_computer_choice() -> str:
    """Randomly choose rock, paper, or scissors for the computer opponent."""
    return random.choice(VALID_CHOICES)


def determine_winner(player_choice: str, computer_choice: str) -> str:
    """Return the outcome for the player: win, lose, or tie."""
    if player_choice == computer_choice:
        return "tie"

    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if wins_against[player_choice] == computer_choice:
        return "win"
    return "lose"


def play_round() -> str:
    player_choice = get_player_choice()
    if player_choice == QUIT_OPTION:
        return QUIT_OPTION

    computer_choice = get_computer_choice()
    print(f"You chose: {player_choice}")
    print(f"Opponent chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    if result == "win":
        print("You win this round!")
    elif result == "lose":
        print("You lose this round.")
    else:
        print("This round is a tie.")

    return result


def play_game() -> None:
    print("Welcome to Rock, Paper, Scissors!")
    print("Play against the computer opponent.")

    score = {"win": 0, "lose": 0, "tie": 0}

    while True:
        result = play_round()
        if result == QUIT_OPTION:
            print("\nQuitting game.")
            break

        score[result] += 1

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            break

    print("\nGame over.")
    print(f"Wins: {score['win']}")
    print(f"Losses: {score['lose']}")
    print(f"Ties: {score['tie']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_game()
qu