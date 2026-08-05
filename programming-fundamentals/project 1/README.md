# MNK — Project 1 (Fundamentals of Programming, IST)

Python implementation of an m,n,k board game (a generalization of Tic-Tac-Toe and
Gomoku) where a human player competes against the computer.

## What it does
- Represents the board as a tuple of tuples and positions as integers.
- Lets a human player choose moves manually.
- Implements three computer opponent strategies of increasing difficulty:
  - **Easy** — plays adjacent to its own pieces, or a random free position.
  - **Normal** — plays to extend its own longest line or block the opponent's.
  - **Hard** — checks for immediate wins/blocks, then simulates full games ahead
    to pick the best possible outcome.
- Runs a complete game loop, printing the board and announcing the result
  (win/loss/draw).

## Notes
Built entirely with functions and built-in Python types (tuples), no external
libraries — this was a constraint of the assignment.
