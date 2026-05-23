# Rock, Paper, Scissors Console Game

This project contains a simple Python console game where you play rock-paper-scissors against the computer.

## Game behavior

- The player chooses one of: `rock`, `paper`, or `scissors`.
- The computer randomly selects one of the same options.
- The game displays whether the player wins, loses, or ties each round.
- The player can type `quit` at any move prompt to exit immediately.
- After each round, the player can choose to play again.
- When the game ends, the final score is displayed with total wins, losses, and ties.

## Run the game

```bash
python app.py
```

## Notes

- Input is case-insensitive and trimmed of extra spaces.
- Invalid choices are rejected with a warning and the player is prompted again.