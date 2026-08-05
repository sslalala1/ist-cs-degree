# Orbito-n — Project 2 (Fundamentals of Programming, IST)

Python implementation of Orbito, a two-player abstract board game played on a
board of concentric "orbits," adapted to a configurable number of orbits (n).

## What it does
- Defines three Abstract Data Types (ADTs) — `posicao` (position), `pedra`
  (stone/piece), and `tabuleiro` (board) — each with constructors, selectors,
  recognizers, and transformers, respecting proper abstraction barriers.
- Implements the core game rule: each turn, a player places a stone, then all
  stones on the board rotate one step counter-clockwise within their orbit.
- Supports two computer strategies (easy, normal) and a two-player mode.
- Runs a full game loop with board rendering and win/draw detection.

## Notes
Focused on data abstraction — a step up in complexity from Project 1, moving from
plain tuples to designed ADTs with enforced abstraction barriers.
